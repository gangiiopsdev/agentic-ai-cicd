from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and argument substitution
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}

@app.get("/ping")
def ping_route(host: str):
    try:
        return ping(host)
    except Exception as e:
        return {"error": str(e)}, 500