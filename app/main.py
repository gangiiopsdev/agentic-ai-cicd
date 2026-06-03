from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        args = ['ping', '--'] + [host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if '@' in host or '&' in host or ';' in host or '`' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)