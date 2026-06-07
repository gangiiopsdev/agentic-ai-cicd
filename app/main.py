from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize the host input
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}