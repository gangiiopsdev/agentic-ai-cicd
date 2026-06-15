from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']
    if host in allowed_hosts:
        return subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    else:
        raise ValueError('Host not allowed')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}