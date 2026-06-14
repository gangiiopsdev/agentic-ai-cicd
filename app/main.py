from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    return ''.join(e for e in host if e.isalnum() or e in ' .-')[:50]

@app.get(
)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        raise ValueError("Invalid host name")

    # Fixed implementation using shlex.quote to prevent command injection
    subprocess.call(["ping", shlex.quote(sanitized_host)])

    return {"status": "completed"}