from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with list of arguments
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def get_ping(status_code=200):
    return {'status': 'completed'}