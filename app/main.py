from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if host.isalnum():
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return f'Ping failed: {e}'

@app.get("/ping")
def ping_endpoint(host: str):
    return {'status': ping(host)}