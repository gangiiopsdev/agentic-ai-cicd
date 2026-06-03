from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host: str):
    # Basic escaping for demonstration purposes. In production use a secure method.
    return host.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):

    # Secure implementation using subprocess.call with shell=False
    subprocess.call(['ping', escape_host(host)])

    return {"status": "completed"}