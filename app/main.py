from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return 'Invalid hostname'
    args = ['ping', host]
    try:
        output = subprocess.run(args, capture_output=True, text=True)
        return output.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if 'completed' in result:
        return {'status': 'completed', 'result': 'success'}
    else:
        return {'status': 'failed', 'result': result}