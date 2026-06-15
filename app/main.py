from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.Popen
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    status, _ = safe_ping(host)
    return {"status": "completed", "output": status}