from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using subprocess.run without shell=True
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get("/ping")
def ping_handler(host: str):
    result = ping(host)
    return {'status': 'completed'}