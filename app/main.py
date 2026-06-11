from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    if host:
        try:
            subprocess.call(['ping', '-c', '1', host], shell=False)
        except Exception as e:
            return {'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)