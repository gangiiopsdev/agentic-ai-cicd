from fastapi import FastAPI
import subprocess
global_safe_hosts = {'google.com', 'example.com'}  # Add more hosts as needed
def safe_ping(host: str):
    if host not in global_safe_hosts:
        raise ValueError('Invalid host')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}