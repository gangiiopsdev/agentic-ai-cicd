from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host'}, 400
    args = ['ping', '-c', '1', host]  # Limit the number of pings to mitigate risks
    subprocess.run(args, check=True)
    return {'status': 'completed'}