from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return input_string.strip()

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    if 'ping' in host:
        return {'error': 'Invalid input'}, 400
    try:
        subprocess.run(['ping', host], check=True, timeout=5, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}, 500