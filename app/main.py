from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    @validator('host')
    def validate_host(v):
        if not v.startswith(('192.168', '172.16', '10.', '::ffff:192.168', '::ffff:172.16', '::ffff:10.')):
            raise ValueError('Invalid host')
        return v

    # Use a safer method to execute ping
    try:
        result = subprocess.run(['ping', '-c', '4', '--'], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}