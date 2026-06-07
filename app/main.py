from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Using subprocess.run instead of subprocess.call for better control and safety
        result = subprocess.run(['ping', '--no-wait', '--quiet', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)