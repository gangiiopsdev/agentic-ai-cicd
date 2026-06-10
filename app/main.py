from fastapi import FastAPI
import subprocess
from shlex import quote
from os.path import join

app = FastAPI()

def safe_ping(host: str):
    quoted_host = quote(host)
    subprocess.run([join('/bin', 'ping'), quoted_host], shell=False, check=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}