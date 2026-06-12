from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        subprocess.call(['ping', host], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)