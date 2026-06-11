from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        response = subprocess.run(['ping', host], check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': response.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    return ping(host)