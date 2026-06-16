from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() and c.isprintable())

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host or len(sanitized_host) > 100:
        return {'status': 'error', 'output': 'Invalid host'}
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}
    except Exception as e:
        return {'status': 'error', 'output': str(e)}