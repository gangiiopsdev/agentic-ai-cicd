from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> bool:
    return host.isalnum() and len(host) <= 255

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if safe_ping(host):
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'stderr': e.stderr}
    else:
        return {'status': 'invalid input'}