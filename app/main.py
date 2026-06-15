from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_route(host: str):
    result = ping(host)
    return {"status": "completed", "result": result}