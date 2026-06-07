from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping_host(host: str):
    return ping(host)