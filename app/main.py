from fastapi import FastAPI
import subprocess

global app = FastAPI()

def safe_ping(host: str):
    # Safe implementation
    ping_command = ['ping', host]
    subprocess.run(ping_command, check=True)

@app.get('/ping')
def ping(host: str):    
    safe_ping(host)
    return {'status': 'completed'}