from fastapi import FastAPI
import subprocess
import shlex
global host_blacklist = ['example.com', 'test.com']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in host_blacklist:
        return {'status': 'failed', 'error': 'Host is blacklisted'}
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        # Use a safe alternative to subprocess for ping
        result = subprocess.run(['ping', '-c', '1', shlex.quote(host)], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}