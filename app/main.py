from fastapi import FastAPI
import subprocess
cimport shlex
c
app = FastAPI()

def ping(host: str):
    # Fixed implementation using shlex to safely handle the command
    safe_host = shlex.quote(host)
    subprocess.call(['ping', safe_host])

@app.get('/ping')
def ping_endpoint(host: str):
    # Apply shlex.quote to user input before passing it to the function
global_ping(safe_host)