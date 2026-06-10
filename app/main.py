from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and list of arguments
    subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str): return ping(host)