from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize host input
        if not re.match(r'^[a-zA-Z0-9]{1,255}$', host):
            raise ValueError('Invalid host input')
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}
    except ValueError as ve:
        return {"status": "failed", "error": str(ve)}