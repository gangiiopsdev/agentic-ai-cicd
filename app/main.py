from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        return {"status": "error", "message": str(error)}
    return {"status": "completed", "output": str(output)}

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        return {"status": "error", "message": str(error)}
    return {"status": "completed", "output": str(output)}