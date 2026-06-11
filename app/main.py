from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.strip() == 'localhost':
        return True
    return False

@app.get('/ping')
def ping(host: str):
    if not safe_ping(host):
        return {'error': 'Invalid or restricted host'}
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}