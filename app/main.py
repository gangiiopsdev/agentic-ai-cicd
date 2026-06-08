from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Implement proper sanitization logic here
    return host.strip()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    result = subprocess.run(["ping", sanitized_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}