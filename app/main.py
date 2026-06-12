from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Validate host to ensure it is a valid IP address or hostname
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return 'Invalid input'
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Failed to ping {host}: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)