from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    @staticmethod
def run(host):
        # Validate and sanitize the input to prevent command injection
        try:
            host = shlex.quote(host)
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    return SafePing.run(host)