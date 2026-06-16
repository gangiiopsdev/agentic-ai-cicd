from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command(input):
    return input.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}