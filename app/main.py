from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    # Use a whitelist of allowed hosts or validate input strictly
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Unauthorized host'}
    try:
        output = subprocess.check_output(['ping', host], universal_newlines=True, timeout=10)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)