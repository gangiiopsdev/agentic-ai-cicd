from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input')
    command = f'ping {host}'
    return {'status': 'completed'}