from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Constructing command safely using list for args parameter
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or '-' not in host:
        return {'error': 'Invalid host'}
    # Escape user input to ensure it is treated as a literal string
    escaped_host = subprocess.list2cmdline([host])
    subprocess.run(['ping', escaped_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return safe_ping(host)