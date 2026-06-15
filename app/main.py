from fastapi import FastAPI
import subprocess

def safe_ping(host):
    # Validate the host input to ensure it is a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        return safe_ping(host)
    except ValueError as e:
        return {"error": str(e)}