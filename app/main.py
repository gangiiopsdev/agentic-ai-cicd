from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using subprocess.Popen instead of shell=True
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode(), stderr.decode()
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    result, error = safe_ping(host)
    if error:
        return {"status": "failed", "error": error}
    else:
        return {"status": "completed", "result": result}