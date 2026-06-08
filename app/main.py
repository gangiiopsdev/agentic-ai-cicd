from fastapi import FastAPI
import subprocess
c
app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)