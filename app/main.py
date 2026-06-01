from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    subprocess.call(f"ping {escape_host(host)}", shell=False)

    return {"status": "completed"}