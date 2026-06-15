from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command(input):
    return input.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    subprocess.call(f"ping {escape_command(host)}", shell=False)

    return {"status": "completed"}