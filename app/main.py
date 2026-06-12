from fastapi import FastAPI
import subprocess
global hosts
hosts = set()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in hosts:
        hosts.add(host)
    else:
        return {"status": "host already checked"}
    
    # Fixed implementation
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {"status": "completed", "result": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}