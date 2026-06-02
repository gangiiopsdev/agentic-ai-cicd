from fastapi import FastAPI
import subprocess
from typing import Optional

def sanitize_input(input_str: str) -> str:
    return ''.join(char for char in input_str if char.isalnum() or char.isspace())

app = FastAPI()

@app.get("/ping")
def ping(host: str) -> dict:
    sanitized_host = sanitize_input(host)
    try:
        # Validate the input to ensure it does not contain malicious content
        if any(char in sanitized_host for char in [';', '&', '|', '&&', '||']):
            return {"status": "failed", "error": "Invalid characters in input"}
        subprocess.run(["ping", sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        return {"status": "failed", "error": str(e)}

    return {"status": "completed"}