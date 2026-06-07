from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', '-c', '1', shlex.quote(host)], universal_newlines=True, timeout=10)
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/"付费试用)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)