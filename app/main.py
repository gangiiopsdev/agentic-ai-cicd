from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'host': host, 'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'host': host, 'error': e.stderr}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)