from fastapi import FastAPI
import subprocess
global pings = set()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in pings:
        pings.add(host)
        # Use subprocess.run with a list to avoid shell injection risk
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}