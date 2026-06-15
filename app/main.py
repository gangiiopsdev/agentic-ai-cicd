from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    return {'status': 'completed', 'result': safe_ping(host)}

# Preventive control to validate the host input
def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Add more valid hosts as needed
    return any(h in host for h in allowed_hosts)