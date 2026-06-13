from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        response = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': response.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping_host(host: str):
    return ping(host)