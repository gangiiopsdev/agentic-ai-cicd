from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    args = ['ping', host]
    subprocess.run(args, shell=False)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    execute_ping(host)
    return {"status": "completed"}