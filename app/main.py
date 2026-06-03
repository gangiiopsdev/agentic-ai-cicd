from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, check=True)
    return {'status': 'completed', 'exitcode': result.returncode}

@app.get('/ping')
def ping_route(host: str): # Renamed function to avoid conflict with the built-in ping command
    return ping(host)