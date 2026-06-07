from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')

@app.get('/ping')
def ping(host: str):