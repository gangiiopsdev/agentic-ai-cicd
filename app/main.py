from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return output.decode().strip()
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output.decode()}'

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': safe_ping(host)}