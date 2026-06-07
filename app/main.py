from fastapi import FastAPI
import subprocess
class SafePinger:
    @staticmethod
    def ping(host: str):
        if not host.strip():
            return "Invalid input"
        # Use of f-string to safely include user input in the command
        safe_host = host
        subprocess.call(['ping', safe_host])
        return {"status": "completed"}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return SafePinger.ping(host)