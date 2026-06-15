from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', '-c', '1', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    try:
        return ping(host)
    except subprocess.CalledProcessError as e:
        return {"error": "Ping failed", "details": str(e)}