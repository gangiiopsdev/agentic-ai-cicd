from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'another-example.com']  # Define allowed hosts
    if host in allowed_hosts:
        args = ['ping', shlex.quote(host)]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'failed', 'message': 'Host not allowed'}

@app.get("/ping")
def ping(host: str):
    if shlex.quote(host) == host and host in allowed_hosts:
        return safe_ping(host)
    else:
        return {'status': 'failed', 'message': 'Invalid or unauthorized host'}