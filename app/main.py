from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    def ping(self, host: str):
        command = ['ping', *shlex.split(host)]
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
        return {'status': 'completed'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    service = PingService()
    return service.ping(host)