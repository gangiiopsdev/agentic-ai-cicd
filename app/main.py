from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.Popen instead of shell=True
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output, error = safe_ping(host)
        if error:
            return {"status": "failed", "error": error.decode()}
        else:
            return {"status": "completed", "output": output.decode()}
    except Exception as e:
        return {"status": "exception", "message": str(e)}