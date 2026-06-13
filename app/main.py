from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if '.' not in host and ':' not in host:
        return 'Invalid host'
    args = ['ping', '-c', '1', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return 0 if process.returncode == 0 else -1

global_app = FastAPI()

@global_app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@global_app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result == 0:
        return {"status": "completed", "result": "Success"}
    else:
        return {"status": "failed", "result": "Failed"}