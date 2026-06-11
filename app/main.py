from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE)
    return {'output': result.stdout.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)