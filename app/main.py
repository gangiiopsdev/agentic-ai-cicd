from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command(input):
    return ''.join(c for c in input if c.isalnum() or c in ['-', '.', ':', '/'])

@app.get("/ping")
def ping(host: str):
    safe_host = escape_command(host)
    args = ['ping', '-c', '1', safe_host]
    subprocess.run(args, check=True)
    return {"status": "completed"}