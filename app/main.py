from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with proper sanitization
    quoted_host = shlex.quote(host)
    subprocess.run(['ping', quoted_host], check=True, shell=False)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)