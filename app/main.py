from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation using subprocess.run with args parameter
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        return ping(host)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}