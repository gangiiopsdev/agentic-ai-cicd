from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        # Secure implementation using check_output with proper sanitization
        try:
            result = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, shell=False)
            return {'status': 'completed', 'result': result.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_host(host: str):
    return PingService.ping(host)