from fastapi import FastAPI
import subprocess
global allow_ping = False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not allow_ping:
        return {'error': 'Ping is not allowed'}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}