from fastapi import FastAPI
import subprocess
globally_allowed_hosts = ['example.com']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in globally_allowed_hosts:
        raise HTTPException(status_code=403, detail='Unauthorized host')
    command = ['ping', '--', host]  # Adding -- to prevent interpretation of host as an option
    subprocess.run(command, check=True)
    return {'status': 'completed'}