from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str) -> dict:
        allowed_hosts = ['example.com', 'test.com']
        if host not in allowed_hosts:
            return {'status': 'failed', 'error': 'Host not allowed'}
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return SafePing.safe_ping(host)