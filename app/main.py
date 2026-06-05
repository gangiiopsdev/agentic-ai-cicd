from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Secure implementation using a list for the command arguments
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):    
    if not host.isalnum():
        return {"status": "failed", "error": "Invalid input"}
    try:
        run_ping(host)
        return {"status": "completed", "message": "Ping successful"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}