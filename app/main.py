from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        try:
            subprocess.run(['ping', host], capture_output=True, text=True)
            return {'status': 'completed'}
        except Exception as e:
            return {'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return SafePing.safe_ping(host)