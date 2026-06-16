from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        subprocess.call(['ping', host], shell=False)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)