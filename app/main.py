from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def get_ping(host: str): 
    return ping(host)