from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Using safe subprocess call without shell=True
        subprocess.call(['ping', host], timeout=5)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)