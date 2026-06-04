from fastapi import FastAPI, HTTPException
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise HTTPException(status_code=400, detail="Invalid host")
    command = ['ping', '-c', '1'] + shlex.split(host)
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {'host': host, 'result': result.stdout}

@app.get("/ping")
def ping_endpoint(request):
    return ping(request.query_params.get('host'))