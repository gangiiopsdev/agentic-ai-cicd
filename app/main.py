from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host:
        raise ValueError('Host parameter cannot be empty')
    if not host.isalnum() or len(host) > 255:
        raise HTTPException(status_code=400, detail='Invalid host name')
    args = ['ping', '-c', '1', subprocess.list2cmdline([host])]
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode('utf-8')}