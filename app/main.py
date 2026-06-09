from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_hostname(host):
    return host and all(char.isalnum() or char in [".", "-"] for char in host)

@app.get('/ping')
def ping(host: str):
    if is_safe_hostname(host):
        subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}