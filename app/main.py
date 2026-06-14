from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use a whitelist of allowed hosts or validate host input
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        args = ['ping', '--'] + [host]  # Add -- to avoid command injection
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'result': result}
    except ValueError as e:
        return {'error': str(e)}