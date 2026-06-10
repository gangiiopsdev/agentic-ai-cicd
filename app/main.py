from fastapi import FastAPI
import subprocess
import re
def sanitize_input(input_string):
    return re.sub(r'[;`|&*?~<>{}()\/$]', '', input_string)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
        return {"status": "invalid_host"}
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}