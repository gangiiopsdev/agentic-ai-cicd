from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using list of arguments
    subprocess.call(['ping', host])

@app.get('/ping')
def ping(host: str):
    safe_ping(subprocess.quote(host))
    return {'status': 'completed'}