from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    try:
        args = shlex.split('ping ' + host)
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error: {e}'}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)