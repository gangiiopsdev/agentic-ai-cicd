from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {str(e)}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() or '-' not in host:
        return 'Invalid hostname'
    sanitized_host = subprocess.quote(host)
    return run_ping(sanitized_host)