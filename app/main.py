from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host format and length
    if not re.match(r'^[a-zA-Z0-9]{1,64}$', host):
        return {"status": "error", "message": "Invalid input"}
    result = subprocess.run(['ping', f'--{host}'], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}