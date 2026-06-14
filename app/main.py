from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output}
    else:
        return {'status': 'failed', 'error': 'Unauthorized host'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)