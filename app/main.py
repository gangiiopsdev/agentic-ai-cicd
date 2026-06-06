from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    # Safe implementation
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    execute_ping(host)

    return {"status": "completed"}