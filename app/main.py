from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using Popen and list of arguments
    args = ['ping', '-c', '1', '--', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error
global app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result, err = safe_ping(host)
    if err:
        return {"status": "error", "message": err.decode()}
    else:
        return {"status": "completed", "result": result.decode()}