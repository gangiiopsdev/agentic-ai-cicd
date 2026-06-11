from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host and any(char in host for char in ' ;&|*?~<>^()[]{}$\'):  # Basic validation
        return "Invalid input"
    subprocess.call(f'ping {host}', shell=False)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict):
        return result
    else:
        return {"status": "completed", "message": result}