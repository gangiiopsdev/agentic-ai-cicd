from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    run_ping(host)
    return {"status": "completed"}