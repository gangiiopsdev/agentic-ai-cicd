from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation with input validation and use of check_output instead of call
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        raise ValueError("Invalid hostname")
    try:
        result = subprocess.run(['ping', '-c', '1', f'/bin/ping {host}'], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

@app.get('/ping')
def ping_endpoint(host: str):
    return await ping(host)

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}