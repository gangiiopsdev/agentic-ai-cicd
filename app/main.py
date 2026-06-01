from fastapi import FastAPI
import subprocess
from shlex import quote

global app = FastAPI()

async def escape_input(user_input):
    return quote(user_input)

@app.get("/ping")
def ping(host: str):
    escaped_host = await escape_input(host)
    subprocess.run(['ping', '-c', '1', escaped_host], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": subprocess.stdout}