from fastapi import FastAPI
import shlex

app = FastAPI()

def ping(host: str):
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return {'result': 'Pinging ' + host}