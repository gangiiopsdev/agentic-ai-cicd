from fastapi import FastAPI
import subprocess
def escape_host(host: str) -> str:
    # Simple escaping for demonstration purposes
    return host.replace(";", "_").replace("&", "_")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    args = ["ping", escaped_host]
    subprocess.run(args, check=True)
    return {"status": "completed"}