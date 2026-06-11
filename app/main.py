from fastapi import FastAPI, HTTPException
import subprocess
import shlex

global_blacklist = [';', '&', '|', '`']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or any(char in host for char in global_blacklist):
        raise HTTPException(status_code=400, detail='Invalid input detected')
    try:
        # Sanitize the host input to prevent shell injection
        output = subprocess.run(['ping', '--', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e))