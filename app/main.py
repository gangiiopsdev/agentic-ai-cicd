from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Sanitize host input
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout,
app = FastAPI()
@app.get("/ping")
def ping(host: str):    return {'status': safe_ping(host)[0]}