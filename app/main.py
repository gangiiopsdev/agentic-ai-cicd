from fastapi import FastAPI
import subprocess
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    allowed_hosts = ['example.com', 'another-example.com']
    if host not in allowed_hosts:
        return {'error': 'Invalid host'}, 403

    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}