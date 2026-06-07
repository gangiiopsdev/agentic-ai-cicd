from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        subprocess.run(['ping', host], check=True, shell=False)
    except Exception as e:
        return {'error': str(e)}

@app.get("/ping")
def ping_route(host: str):    return ping(host)