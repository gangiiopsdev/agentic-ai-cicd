from fastapi import FastAPI
import subprocess
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input
    if not host.isalnum():
        return {'status': 'error', 'response': 'Invalid input'}

    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'response': jsonable_encoder(result.stdout)}