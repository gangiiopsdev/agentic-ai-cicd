from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate the host input to ensure it's a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')
    args = ["ping", shlex.quote(host)]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return {'result': 'Pinging ' + host}