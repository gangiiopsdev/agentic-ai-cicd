from fastapi import FastAPI
import subprocess
global allow_hosts = ['example.com']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host or '&&' in host or ';' in host or host not in allow_hosts:
        return {'error': 'Invalid input'}
    subprocess.run(['ping', subprocess.check_output(f"echo {host}").decode().strip()], check=True, capture_output=True, text=True)
    return {'status': 'completed'}