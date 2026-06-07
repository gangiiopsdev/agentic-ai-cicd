from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

def sanitize_input(input_string):
    # Implement your sanitization logic here, e.g., regex validation
    return ''.join(c for c in input_string if c.isalnum())

@app.get("/ping")
def ping(host: str = validator(sanitize_input)):
    try:
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}