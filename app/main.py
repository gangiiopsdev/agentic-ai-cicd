from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], shell=False)

@app.get("/ping")
def ping_endpoint(host: str):
    return {'result': 'Pinging ' + host}