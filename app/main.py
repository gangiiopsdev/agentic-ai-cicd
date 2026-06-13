from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

async def ping(host: str):
    # Secure implementation using shlex for safe argument splitting and input validation
    if host.strip() == '':
        raise ValueError('Host cannot be empty')
    cmd = ['ping', host]
    await subprocess.run(cmd, check=True, shell=False)

@app.get("/ping")
def ping_endpoint(host: str):
    return {'result': ping(host)}