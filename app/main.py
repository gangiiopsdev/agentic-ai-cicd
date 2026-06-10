from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        try:
            subprocess.run(['ping', host], check=True, shell=False)
            return 'Ping successful'
        except subprocess.CalledProcessError as e:
            return f'Ping failed with error {e.returncode}

app = FastAPI()

def ping_route(host: str):
    service = PingService()
    return service.ping(host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}