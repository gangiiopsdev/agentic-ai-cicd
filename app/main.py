from fastapi import FastAPI
import subprocess
def escape_host(host: str) -> str:
    return ''.join(c for c in host if c.isalnum() or c.isdigit())

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = escape_host(host)
    if not sanitized_host:
        raise ValueError("Invalid host name")
    try:
        result = subprocess.run(["ping", "-c", 1, sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}