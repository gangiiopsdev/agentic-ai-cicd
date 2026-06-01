from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host: str):
    # Secure implementation using subprocess.run instead of shell=True
    try:
        subprocess.run(['ping', host], check=True, text=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    return _ping(host)