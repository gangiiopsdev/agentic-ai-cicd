from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not validate_host(host):
        raise ValueError('Invalid host provided')
    return run_ping(host)

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., allow only certain domain names or IP addresses
    allowed_hosts = ['example.com', '192.168.1.1']
    return host in allowed_hosts