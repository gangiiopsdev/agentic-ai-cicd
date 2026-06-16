from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if re.match(r'^[0-9]+$', host):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"error": "Invalid input for ping command"}