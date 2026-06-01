from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):  
    return ping(host)