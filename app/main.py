from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.Popen
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)