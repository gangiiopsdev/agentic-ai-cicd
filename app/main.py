from fastapi import FastAPI
import subprocess
getoutput = subprocess.getoutput
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = getoutput(f'ping {host}')
    return {'status': 'completed', 'result': result}