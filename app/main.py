from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return f'Error: {e}'

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_host(host: str):
    ping_service = PingService()
    return ping_service.ping(host)