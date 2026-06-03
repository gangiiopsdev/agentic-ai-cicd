from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host or 'ping' not in host:
        return False
    args = ['ping', subprocess.check_output(['echo', host], text=True).strip()]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)