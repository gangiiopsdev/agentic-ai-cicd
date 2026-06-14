from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)