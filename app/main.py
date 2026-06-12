from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote to escape arguments
    command = ['ping', shlex.quote(host)]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with exit code {e.returncode}'}, 500

@app.get("/ping")
def ping_route(host: str):
    return ping(host)