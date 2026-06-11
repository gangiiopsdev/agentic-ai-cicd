from fastapi import FastAPI
import subprocess
global ALLOWED_HOSTS = ['localhost', '127.0.0.1']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in ALLOWED_HOSTS:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'error': 'Host not allowed'}