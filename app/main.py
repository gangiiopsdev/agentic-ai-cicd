from fastapi import FastAPI
import subprocess
global _ping_cache = {}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent injection attacks
    if not host.isalnum() or ' ' in host:
        return {"error": "Invalid input"}, 400
    if host in _ping_cache:
        return {"status": "completed", "cache_hit": True}
    subprocess.call(['ping', '-c', '1', host])
    _ping_cache[host] = True
    return {"status": "completed"}