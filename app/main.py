from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host):
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return _ping(host)