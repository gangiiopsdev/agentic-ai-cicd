from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    # Validate input to prevent command injection
    if not host or not isinstance(host, str) or ' ' in host:
        return "Invalid input"
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get('/ping')
def ping(host: str):
    # Validate input further to prevent shell injection
    if '&&' in host or ';' in host or '|' in host or '`' in host or '$' in host:
        return "Invalid input"
    return execute_ping(host)