from fastapi import FastAPI
import subprocess
def is_valid_host(host):
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return all(char in valid_chars for char in host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    output = subprocess.check_output(['ping', host], shell=False, timeout=5)
    return {'status': 'completed', 'output': output.decode()}