from fastapi import FastAPI
import subprocess
globally_whitelisted_hosts = ['host1', 'host2']  # Define a list of allowed hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in globally_whitelisted_hosts:
        subprocess.run(['ping', host], check=True)
    else:
        return {'error': 'Host not allowed'}, 403
    return {'status': 'completed'}