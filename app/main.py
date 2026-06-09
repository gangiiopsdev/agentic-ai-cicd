from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    try:
        result = subprocess.run(['ping', host], check=True, text=True, capture_output=True)
        return {'stdout': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)