from fastapi import FastAPI
import subprocess
class SafePinger:
    @staticmethod
def safe_ping(host: str) -> dict:
        if not host.isalnum() or len(host) > 100:
            return {'status': 'error', 'message': 'Invalid host'}
        args = ['ping', host]
        result = subprocess.Popen(args, stdout=subprocess.PIPE)
        output, _ = result.communicate()
        return {'status': 'completed', 'output': output.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return SafePinger.safe_ping(host)