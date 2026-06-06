from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return ping(host)