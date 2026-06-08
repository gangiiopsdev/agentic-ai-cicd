from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if 'ping' in host or any(char in host for char in [';', '&', '|', '*', '?', '<', '>']):
        return {"error": "Invalid input detected"}
    args = ['ping', '{}'.format(host)]
    subprocess.run(args, check=True)
    return {"status": "completed"}