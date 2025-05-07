
---

### **3. Would it work in GitLab CI?**

Yes, **but only if SSH forwarding is set up properly in the CI job**, which **is tricky** and requires care.

#### 🧩 GitLab CI Setup Caveats:
- GitLab runners **don’t have an SSH agent by default**.
- You’ll need to:
  - Store the private key in a **CI secret variable**.
  - Inject it in the job and configure `ssh-agent`.
  - Use `--ssh` with BuildKit to forward the key.

#### ✅ Basic working example for GitLab CI:

```yaml
variables:
  DOCKER_BUILDKIT: 1

build:
  image: docker:latest
  services:
    - docker:dind
  before_script:
    - apk add --no-cache openssh-client
    - mkdir -p ~/.ssh
    - echo "$SSH_PRIVATE_KEY" | tr -d '\r' > ~/.ssh/id_ed25519
    - chmod 600 ~/.ssh/id_ed25519
    - eval $(ssh-agent -s)
    - ssh-add ~/.ssh/id_ed25519
    - ssh-keyscan gitlab.teadal.ubiwhere.com >> ~/.ssh/known_hosts
  script:
    - docker build --ssh default -t sfdp-med-gl:ci -f Dockerfile_from_src .
