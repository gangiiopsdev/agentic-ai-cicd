from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def escape_shell_arg(arg):
    return ' '.join(quote(arg))

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(f"ping {escape_shell_arg(host)}", shell=False)
    return {"status": "completed"}