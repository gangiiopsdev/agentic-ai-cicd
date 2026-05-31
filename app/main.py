from fastapi import FastAPI
import subprocess
from sanic.response import text

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return text('Invalid input', status=400)
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}