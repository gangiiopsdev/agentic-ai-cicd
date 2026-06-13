from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    subprocess.run(['ping', host], capture_output=True, text=True, check=True)

@app.get("/ping")
def ping_route(host: str):
    return {'host': host, 'result': ping(host)}