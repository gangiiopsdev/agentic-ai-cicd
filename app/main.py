from fastapi import FastAPI
import subprocess
class Sanitize:
    @staticmethod
def sanitize_host(host: str) -> bool:
        return all(c.isalnum() or c in ['.', '-'] for c in host)

app = FastAPI()

def ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/" )
def home():
    return {"message": "Agentic Self-Healing Pipeline" }

@app.get("/ping")
def ping_host(host: str):
    if Sanitize.sanitize_host(host):
        return ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}