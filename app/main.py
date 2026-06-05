from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    from shlex import quote
    subprocess.run(['ping', quote(host)], check=True)