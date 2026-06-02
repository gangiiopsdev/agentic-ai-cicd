from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    return SafePing.ping(host)