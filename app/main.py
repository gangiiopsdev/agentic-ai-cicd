from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}