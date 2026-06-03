from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(input_str):
    if not input_str.strip().isalnum():
        raise ValueError("Invalid input")

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = quote(host)
        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}
    except ValueError as e:
        return {"status": "failed", "error": str(e)}