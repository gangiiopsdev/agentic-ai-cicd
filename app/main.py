from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping/{host}")
def ping(host: str):
    # Secure implementation
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        raise ValueError('Invalid hostname')
    command = ['ping', subprocess.list2cmdline([host])]
    result = subprocess.run(command, check=True)
    return {'status': 'completed'}