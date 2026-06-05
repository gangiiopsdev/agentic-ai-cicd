from fastapi import FastAPI
import subprocess
dfrom shlex import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation using shlex.quote to safely escape the input
    subprocess.call(['ping', quote(host)])
    return {'status': 'completed'}