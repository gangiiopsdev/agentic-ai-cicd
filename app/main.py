from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_endpoint(host: str):
    response = ping(host)
    return {"status": "completed", "response": response}