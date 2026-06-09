from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    @staticmethod
def run_safe_ping(host: str) -> dict:
        # Sanitize the host input using shlex.quote
        safe_host = shlex.quote(host)
        try:
            result = subprocess.run(['ping', safe_host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return SafePing.run_safe_ping(host)