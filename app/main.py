from fastapi import FastAPI
import subprocess
import shlex
def escape_input(user_input):
    return ' '.join(shlex.quote(x) for x in user_input.split())
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    escaped_host = escape_input(host)
    # Safe implementation
    subprocess.call(['ping', escaped_host])