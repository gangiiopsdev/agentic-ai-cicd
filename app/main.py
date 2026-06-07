from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'Invalid host'}
    result = os.system(f'ping {host}')
    if result == 0:
        return {'status': 'Ping successful'}
    else:
        return {'status': 'Ping failed'}