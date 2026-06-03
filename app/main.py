from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize host input
    if not is_valid_host(host):
        return {"status": "invalid host"}
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Simple validation example, can be more complex
    return '.' in host and '@' not in host