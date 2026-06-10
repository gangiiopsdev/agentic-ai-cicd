from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple validation to ensure only alphanumeric characters are used
    return ''.join(c for c in host if c.isalnum() or c in ['.', '-'])

@app.get("/ping")
def ping(host: str):