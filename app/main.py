from fastapi import FastAPI
import subprocess
globally_allowed_hosts = ['example.com']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in globally_allowed_hosts:
        raise HTTPException(status_code=403, detail='Unauthorized host')
    command = ['ping', '--', host]  # Adding -- to prevent interpretation of host as an option
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise HTTPException(status_code=500, detail=result.stderr)
    return {'status': 'completed'}