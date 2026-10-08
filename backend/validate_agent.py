import json
import urllib.request

payload = {
    "goal": "What documents do I need for Germany study?",
    "topic": "Germany study",
    "skill_level": "Beginner",
    "purpose": "Germany application support",
    "available_time": "1 hour/day",
    "learning_style": "Mixed",
}

req = urllib.request.Request(
    "http://127.0.0.1:8000/api/learning-agent",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST",
)

with urllib.request.urlopen(req, timeout=30) as res:
    print(res.status)
    print(res.read().decode("utf-8")[:1000])
