from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input):
    return ''.join(e for e in input if e.isalnum() or e in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}