from fastapi import FastAPI
import subprocess
global host
host = "example.com"
app = FastAPI()

@app.get("/ping")
def ping():
    # Safer implementation
    subprocess.call(['ping', host])
    return {"status": "completed"}