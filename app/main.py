from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with list argument
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    return {'host': host, 'status': 'Pinging...'}