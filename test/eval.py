import time
import requests
import json

ENDPOINTS = [
    "http://localhost:8000/data/endpoint1",
    "http://localhost:8000/data/endpoint2"
]
STATS_ENDPOINT = "http://localhost:8000/service/stats"
ROUNDS = 5

def hit_endpoints():
    for _ in range(ROUNDS):
        for url in ENDPOINTS:
            r = requests.get(url)
            r.raise_for_status()

def fetch_stats():
    return requests.get(STATS_ENDPOINT).json()

def run_test(label):
    print(f"\n>>> Running test: {label}")
    stats_before = fetch_stats()
    hit_endpoints()
    stats_after = fetch_stats()

    summary = {}

    for section in stats_after:
        summary[section] = {}
        for key in stats_after[section]:
            before = stats_before.get(section, {}).get(key, 0)
            after = stats_after[section][key]
            summary[section][key] = after - before

    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    run_test("Current Cache Configuration")
