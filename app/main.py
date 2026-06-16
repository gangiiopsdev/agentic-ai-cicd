from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    return ''.join(filter(str.isalnum, host))[:20]

def execute_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host != host:
        return {'status': 'error', 'message': 'Invalid input'}
    return execute_ping(sanitized_host)