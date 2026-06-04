from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')
    if not all(char in allowed_chars for char in host):
        raise ValueError("Invalid hostname")

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    args = ['ping', host]
    subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode()}