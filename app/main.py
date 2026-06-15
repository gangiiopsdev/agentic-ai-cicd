from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    def ping(self, host: str):
        cmd = ['ping', host]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8'), 'error': result.stderr.decode('utf-8')}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    return ping_service.ping(host)