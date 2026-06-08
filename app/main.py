from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        subprocess.call(['ping', host], shell=False)
    except Exception as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)