from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Use subprocess.run with full path and avoid shell=True
        result = subprocess.run(['/usr/bin/ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def ping(host: str):
    # Call the safe_ping function instead of using subprocess.call
    return {'status': 'completed', 'output': safe_ping(host)}

@app.get('/ping')
def ping_route(host: str):
    # Call the ping function instead of using subprocess.call directly
    return ping(host)