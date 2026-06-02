from fastapi import FastAPI
import subprocess
from pydantic import constr

app = FastAPI()

@app.get("/ping")
def ping(host: constr(min_length=1, max_length=255)):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}