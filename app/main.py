from fastapi import FastAPI
import subprocess
from shlex import quote as shell_quote

app = FastAPI()

def escape_command(input_str):
    return ''.join(c if c.isalnum() else '_' for c in input_str)

@app.get("/ping")
def ping(host: str):
    host = escape_command(host)
    subprocess.call(["ping", shell_quote(host)])
    return {"status": "completed"}