from fastapi import FastAPI
import subprocess
global host
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed"}