from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run for better control and error handling
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'host': host, 'status': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'host': host, 'error': e.stderr}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)