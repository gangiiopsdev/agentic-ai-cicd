from fastapi import FastAPI
import re
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use a whitelist approach to ensure only safe host values are accepted
    allowed_hosts = ['safehost1', 'safehost2']  # Define a list of allowed hosts
    if host in allowed_hosts:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    else:
        return 'Invalid host'

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'result': safe_ping(host)}