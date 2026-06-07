from fastapi import FastAPI
import subprocess
def safe_ping(host):
    cmd = ['ping', host]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if 'ping' in host:
        return {"error": "Invalid input detected."}
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}