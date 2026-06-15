from fastapi import FastAPI
import subprocess
globally_safe_hosts = ['127.0.0.1', '::1']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in globally_safe_hosts:
        raise HTTPException(status_code=403, detail='Unauthorized host')
    subprocess.call(['ping', host])  # Use the safe parameterization of subprocess
    return {'status': 'completed'}