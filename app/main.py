from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using Popen and list of arguments
    if not host.isalnum():
        return None, 'Invalid input'
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result, err = safe_ping(host)
    if err:
        return {"status": "error", "message": err.decode()}
    else:
        return {"status": "completed", "result": result.decode()}