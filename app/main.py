from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.Popen
    subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get("/ping")
def get_ping(host: str):
    return ping(host)