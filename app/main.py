from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if '@' in host or '>' in host or '<' in host:
        return {"status": "error", "error": "Invalid host parameter detected."}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], universal_newlines=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)