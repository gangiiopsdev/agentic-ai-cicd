from fastapi import FastAPI
import subprocess
class PingHandler:
    def __init__(self):
        pass

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation using subprocess.run without shell=True
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}