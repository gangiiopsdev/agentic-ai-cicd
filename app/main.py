from fastapi import FastAPI
import subprocess
from urllib.parse import quote_plus

def run_command(command: str):
    args = command.split()
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = quote_plus(host)
    run_command(f"ping {safe_host}")
    return {"status": "completed"}