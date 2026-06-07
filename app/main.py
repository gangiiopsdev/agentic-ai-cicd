from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        raise ValueError("Invalid hostname or IP address")

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}, 400