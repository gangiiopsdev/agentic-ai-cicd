from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run
    subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):    return {'status': 'completed'}