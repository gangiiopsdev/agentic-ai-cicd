from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host in ['localhost', '127.0.0.1']:  # Example of safe input validation
        return True
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):