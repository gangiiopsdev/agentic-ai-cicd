from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'result': result.stdout.decode(), 'error': None}
    except subprocess.CalledProcessError as e:
        return {'result': None, 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)