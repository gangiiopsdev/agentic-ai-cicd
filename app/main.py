from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
global ping_service
ping_service = PingService()
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    try:
        # Use shlex.split to safely split the host parameter
        safe_host = subprocess.shlex_split(host)[0]
        return ping_service.ping(safe_host)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}