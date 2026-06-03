from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        subprocess.check_call(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)