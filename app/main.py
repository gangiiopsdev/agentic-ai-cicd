from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isnumeric():
        return 'Invalid host'
    try:
        result = subprocess.run(['ping', '-c', str(1), host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)