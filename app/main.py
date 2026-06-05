from fastapi import FastAPI
import re

app = FastAPI()

def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9-._:@]+$', host):
        raise ValueError('Invalid characters in host')
    args = ['ping', '-c', '1', '--'] + [host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}