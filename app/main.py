from fastapi import FastAPI
import re

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, check=True, text=True, capture_output=True)
    return {'output': result.stdout}