from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '.-')

@app.get="/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    args = ['ping', escaped_host]
    subprocess.call(args)

    return {'status': 'completed'}