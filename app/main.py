from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.strip() or '@' in host:
        return {"error": "Host parameter is empty, invalid, or contains special characters"}
    args = shlex.split(f'ping -c 1 {host}')
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}