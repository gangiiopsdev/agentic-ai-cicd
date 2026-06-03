from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    # Add your sanitization logic here
    return ''.join(e for e in input_str if e.isalnum() or e.isdigit())

@app.get("/ping")
def ping(host: str):
    sanitized_host = shlex.quote(sanitize_input(host))
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}