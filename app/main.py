from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        output = subprocess.run(['ping', host], timeout=5, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()
@app.get("/ping")
def ping_route(host: str):
    return ping(host)