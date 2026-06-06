from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize the host input
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        return {'message': 'Invalid host', 'error': 'Host is not allowed'}

    args = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'message': 'Ping command executed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'message': 'Ping command failed', 'error': str(e)}

@app.get("/ping")
def ping_host(host: str):
    return safe_ping(host)