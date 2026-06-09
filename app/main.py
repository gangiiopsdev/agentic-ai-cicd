from fastapi import FastAPI
import re

def safe_ping(host: str):
    # Use a regular expression to validate the hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()
@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}