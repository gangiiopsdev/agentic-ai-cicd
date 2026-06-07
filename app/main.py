from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        if not safe_host_check(host):
            raise ValueError("Invalid host")
        subprocess.call(f"ping {host}", shell=False)

    def safe_host_check(host: str) -> bool:
        # Simple example of a safe check, replace with actual validation logic
        allowed_hosts = ["127.0.0.1", "localhost"]
        return host in allowed_hosts

global ping
ping = SafePing.ping

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        return {"status": safe_ping(host)}
    except ValueError as e:
        return {"error": str(e)}