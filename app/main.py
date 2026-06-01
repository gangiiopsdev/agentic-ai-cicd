from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        if not host:
            return {'status': 'error', 'message': 'Host is required'}
        try:
            # Use a safe way to call subprocess without shell=True
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_route(host: str):
    return PingService.ping(host)