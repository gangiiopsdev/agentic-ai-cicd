from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_input(host)
    subprocess.call(['ping', escaped_host])
    return {"status": "completed"}