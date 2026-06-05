from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"不成
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get(
"/ping")
def ping(host: str):
    # Secure implementation
    if host and '@' not in host:
        try:
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}
    else:
        return {'status': 'failed', 'error': 'Invalid input'}