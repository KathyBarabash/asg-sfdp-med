[05/07/25 10:07:19] INFO     INFO:asg_runtime:Logging initialized for settings.logging=log_level='INFO'                executor.py:46
                             logging_flavor=<LogFlavors.rich: 'rich'> with level=0
Traceback (most recent call last):
  File "/app/app.py", line 12, in lifespan
    executor = await Executor.async_create()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/asg_runtime/executor.py", line 51, in async_create
    f"Response cache: {'enabled' if settings.response_cache.enabled else 'disabled'}, "
                                    ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/asg_runtime/models/settings.py", line 204, in response_cache
    backend_cfg=self._build_backend_cfg(
                ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/asg_runtime/models/settings.py", line 230, in _build_backend_cfg
    return CacheConfigLru(lru_max_items=lru_max_items)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/pydantic/main.py", line 253, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pydantic_core._pydantic_core.ValidationError: 1 validation error for CacheConfigLru
lru_max_items
  Input should be a valid integer [type=int_type, input_value=None, input_type=NoneType]
    For further information visit https://errors.pydantic.dev/2.11/v/int_type

ERROR:    Traceback (most recent call last):
  File "/usr/local/lib/python3.12/site-packages/starlette/routing.py", line 692, in lifespan
    async with self.lifespan_context(app) as maybe_state:
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/contextlib.py", line 210, in __aenter__
    return await anext(self.gen)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/app/app.py", line 12, in lifespan
    executor = await Executor.async_create()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/asg_runtime/executor.py", line 51, in async_create
    f"Response cache: {'enabled' if settings.response_cache.enabled else 'disabled'}, "
                                    ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/asg_runtime/models/settings.py", line 204, in response_cache
    backend_cfg=self._build_backend_cfg(
                ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/asg_runtime/models/settings.py", line 230, in _build_backend_cfg
    return CacheConfigLru(lru_max_items=lru_max_items)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/pydantic/main.py", line 253, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pydantic_core._pydantic_core.ValidationError: 1 validation error for CacheConfigLru
lru_max_items
  Input should be a valid integer [type=int_type, input_value=None, input_type=NoneType]
    For further information visit https://errors.pydantic.dev/2.11/v/int_type

ERROR:    Application startup failed. Exiting.

---
[user]
	name = Katherine Barabash
	email = kathy@il.ibm.com

    
    STEP 5/10: RUN pip install --no-cache-dir -r reqs_from_gh_src.txt
Collecting git+http://****@github.com/KathyBarabash/asg-runtime.git (from -r reqs_from_gh_src.txt (line 3))
  Cloning http://****@github.com/KathyBarabash/asg-runtime.git to /tmp/pip-req-build-k0nhpv7v
  Running command git clone --filter=blob:none --quiet 'http://****@github.com/KathyBarabash/asg-runtime.git' /tmp/pip-req-build-k0nhpv7v
  warning: redirecting to https://github.com/KathyBarabash/asg-runtime.git/
  Resolved http://****@github.com/KathyBarabash/asg-runtime.git to commit f6e671193424ea3ea52e89630db6334bf3612fe5