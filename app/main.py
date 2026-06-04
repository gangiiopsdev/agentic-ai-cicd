from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use subprocess.run to avoid shell injection
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def safe_host_check(host: str):
    allowed_hosts = ['example.com']  # Define a list of allowed hosts
    if host in allowed_hosts:
        return safe_ping(host)
    else:
        return 'Host not allowed'

@app.get("/ping")
def ping(host: str):
    return {'status': safe_host_check(host)}