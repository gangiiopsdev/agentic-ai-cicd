from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host):
    return ''.join(char for char in host if char.isalnum() or char in '._-')

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    # Secure implementation
    command = ['ping', '-c 1', shlex.quote(safe_host)]
    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}