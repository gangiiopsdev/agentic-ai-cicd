from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.check_output(['ping', host], universal_newlines=True, shell=False)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': e.output}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_host(host: str):
    # Sanitize the input to prevent command injection
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        return {'status': 'error', 'message': 'Invalid host'}
    return SafePing.ping(host)