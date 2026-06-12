from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str) -> dict:
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': e.output.decode()}

app = FastAPI()

cping_service = PingService()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return cping_service.ping(host)