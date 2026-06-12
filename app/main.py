from fastapi import FastAPI
import subprocess
from shlex import quote as shell_quote

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', shell_quote(host)])
    return {"status": "completed"}