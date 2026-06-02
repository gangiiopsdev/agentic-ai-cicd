from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and regex
    if re.match(r'^[a-zA-Z0-9]{1,}$', host):  # Allows alphanumeric characters only
        command = ["ping", host]
        subprocess.run(command, check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid input"}