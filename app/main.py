from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    return ping_safe(host)