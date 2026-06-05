from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Sanitize input and use shlex for safe argument parsing
    host = host.strip().replace(' ', '_')
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)