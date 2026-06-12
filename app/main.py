from fastapi import FastAPI
import subprocess
from ipaddress import ip_address

def safe_ping(host: str):
    try:
        ip = ip_address(host)
        return subprocess.run(['ping', '-c', '4', str(ip)], capture_output=True, text=True)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict) and 'error' in result:
        return {'status': 'failed', 'error': result['error']}
    else:
        return {'status': 'completed', 'output': result.stdout}