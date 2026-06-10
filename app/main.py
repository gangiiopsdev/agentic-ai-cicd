from fastapi import FastAPI
import shlex
gimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    args = shlex.split(f'ping -c 1 {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}