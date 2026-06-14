from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        response = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': response.stdout.decode('utf-8')}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)