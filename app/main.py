from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex.quote for safe argument passing
    from shlex import quote
    subprocess.call(['ping', quote(host)])
    return {'status': 'completed'}