from fastapi import FastAPI
import subprocess
def run_ping(host):
    # Secure implementation using subprocess.run()
    subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get="/ping")
def ping(host: str):
    return run_ping(host)