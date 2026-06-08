from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    safe_host = host.strip().replace(';', '')
    subprocess.call(['ping', safe_host])

@app.get("/ping")
def ping_endpoint(host: str):