from fastapi import FastAPI
import os
import subprocess
def is_valid_host(host):
    # Add validation logic here
    return host.strip()

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):