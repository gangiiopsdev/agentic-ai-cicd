from fastapi import FastAPI
import subprocess
import re
import shlex
class CommandSanitizer:
    @staticmethod
def sanitize_command(command: str) -> str:
        return ' '.join(shlex.quote(arg) for arg in shlex.split(command))

app = FastAPI()

def validate_host(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid input")

async def safe_ping(host: str):
    validate_host(host)
    try:
        result = subprocess.run(f'ping -c 1 {host}', capture_output=True, text=True, timeout=5, check=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    try:
        return await safe_ping(host)
    except ValueError as e:
        return {"error": str(e)}