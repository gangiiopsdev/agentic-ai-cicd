from fastapi import FastAPI
import subprocess
def run_safe_ping(host):
    # Validate the host input to ensure it is safe
    if not validate_host(host):
        raise ValueError('Invalid host input')
    args = ['ping', host]
    try:
        output = subprocess.check_output(args, shell=False)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/" )
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return run_safe_ping(host)

def validate_host(host):
    # Add validation logic here, e.g., whitelist allowed hosts
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts