from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Use subprocess.run instead of subprocess.call and avoid shell=True
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host):
    if not all(char.isalnum() or char in '.-:' for char in host):
        raise ValueError('Invalid hostname')

@app.get('/ping')
def ping_route(host: str):
    validate_host(host)
    return {'status': 'completed', 'output': safe_ping(host)}