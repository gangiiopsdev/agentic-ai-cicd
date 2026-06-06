from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Add your sanitization logic here, e.g., allowed_hosts = ['127.0.0.1', 'localhost']; return host if host in allowed_hosts else None

@app.get('/ping')
def ping(host: str):