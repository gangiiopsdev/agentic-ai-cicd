from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)

def secure_ping(host: str):
    # Secure implementation with full path and shell=False
    subprocess.run(['/bin/ping', host], check=True, shell=False)

@app.get("/ping")
def ping_endpoint(host: str):
    return {'status': 'completed'}