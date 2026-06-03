from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
def escape_shell_argument(arg):
    return shlex.quote(arg)
@app.get("/ping")
def ping(host: str):
    host = escape_shell_argument(host)
    # Secure implementation
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}