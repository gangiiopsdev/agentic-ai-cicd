from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    command = 'ping -c 4'
    args = shlex.split(command)
    args.append(host)
    subprocess.run(args, check=True)
    return {'status': 'completed'}