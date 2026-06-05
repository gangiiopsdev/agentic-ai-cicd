from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host in allowed_hosts:
        args = shlex.split(f"ping {host}")
        result = subprocess.run(args, check=True, capture_output=True, text=True)  # Capture output and text mode for better error handling
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'denied', 'message': 'Unauthorized host'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)