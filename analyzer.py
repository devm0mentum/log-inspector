import re

SUSPICIOUS = [
    "failed password",
    "invalid user",
    "authentication failure"
]

with open("example.log", "r") as f:
    for line in f:
        if any(keyword.lower() in line.lower() for keyword in SUSPICIOUS):
            print("[!] Suspicious:", line.strip())
