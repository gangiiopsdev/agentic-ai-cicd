from fastapi import FastAPI
import subprocess
from shlex import quote
global app = FastAPI()

async def escape_shell_arg(arg):
    return ' '.join(quote(a) for a in arg.split())

@app.get("/ping")
def ping(host: str):  # Vulnerable implementation
    safe_host = quote(host)
    subprocess.run(['ping', '-c', '1', safe_host], check=True, capture_output=True, text=True)
    return {'status': 'completed'}