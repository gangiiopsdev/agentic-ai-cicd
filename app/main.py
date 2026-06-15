from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Sanitize the input to prevent injection attacks
    allowed_hosts = ['google.com', 'example.com']  # Add more hosts as needed
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}