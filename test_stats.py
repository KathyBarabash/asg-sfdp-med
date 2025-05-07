import pytest
import requests
import time

BASE_URL = "http://localhost:8000"
DATA_ENDPOINTS = ["/data/endpoint1", "/data/endpoint2"]
STATS_URL = f"{BASE_URL}/service/stats"
PURGE_URL = f"{BASE_URL}/service/purge"  # Optional: if you expose cache purge
ROUNDS = 5

@pytest.fixture(scope="function")
def reset_and_get_stats():
    # Optional: purge caches between runs
    try:
        requests.post(PURGE_URL)
    except Exception:
        pass  # in case endpoint not available

    before = requests.get(STATS_URL).json()
    yield before
    after = requests.get(STATS_URL).json()
    return before, after

@pytest.mark.parametrize("config_label", [
    "no_cache",
    "origin_cache_only",
    "response_cache_only",
    "both_caches"
])
def test_cache_config_runtime(reset_and_get_stats, config_label):
    """
    Assumes the app has been started separately with the given config.
    You can hook into the setup to restart the app per config if needed.
    """
    print(f"\nTesting cache config: {config_label}")

    for _ in range(ROUNDS):
        for ep in DATA_ENDPOINTS:
            r = requests.get(f"{BASE_URL}{ep}")
            r.raise_for_status()

    # Retrieve stats diff
    before, after = reset_and_get_stats
    stats_diff = {}

    for section in after:
        stats_diff[section] = {}
        for key in after[section]:
            b = before.get(section, {}).get(key, 0)
            a = after[section][key]
            stats_diff[section][key] = a - b

    # Print or store result
    print(f"Stats diff for config {config_label}:")
    for section, values in stats_diff.items():
        print(f"{section}: {values}")

    # Optional: write results to file or export as JSON/CSV for analysis
