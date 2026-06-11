from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        ping(host)
        return {"status": "completed", "message": "Ping successful"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}