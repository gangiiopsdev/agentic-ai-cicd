from fastapi import FastAPI
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if re.match(r'^[a-zA-Z0-9.-]+$', host) and '.' in host:
        args = ['ping', host]
        return subprocess.run(args, capture_output=True, text=True)
    else:
        return {'error': 'Invalid input'}