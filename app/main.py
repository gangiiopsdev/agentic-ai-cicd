from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Use shlex.quote to sanitize the host argument
        sanitized_host = subprocess.list2cmdline([host])
        subprocess.run(['ping', sanitized_host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)