from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_hostname(hostname):
    import re
    pattern = re.compile(r'^[a-zA-Z0-9.-]{1,255}$')
    return bool(pattern.match(hostname))

@app.get("/ping")
def ping(host: str):
    if not is_valid_hostname(host):
        raise ValueError("Invalid hostname")
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}