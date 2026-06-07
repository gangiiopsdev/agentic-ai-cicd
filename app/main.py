from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    subprocess.run(command, check=True)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)