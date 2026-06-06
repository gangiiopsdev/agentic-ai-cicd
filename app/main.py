from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex.quote to escape the host parameter
    from shlex import quote
    command = ['ping', '-c', '1', quote(host)]
    subprocess.run(command, check=True)