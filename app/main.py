from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command(input):
    return input.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    safe_host = escape_command(host)
    subprocess.call(f"ping {safe_host}", shell=True)
    return {'status': 'completed'}