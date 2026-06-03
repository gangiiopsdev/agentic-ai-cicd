from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        try:
            # Secure implementation using subprocess.run without shell=True
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    return ping_service.ping(host)