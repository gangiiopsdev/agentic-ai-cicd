from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': e.output.decode('utf-8')}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)