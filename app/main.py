from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in ' .-')

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}