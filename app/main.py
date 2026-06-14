from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    subprocess.run(command, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)