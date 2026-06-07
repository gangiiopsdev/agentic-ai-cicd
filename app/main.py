from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    @validator(host)
    def validate_host(value):
        if not value.startswith('192.168.') and not value.startswith('10.'):  # Replace with allowed hosts
            raise ValueError("Invalid host")
        return value

    command = ["ping", host]
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}