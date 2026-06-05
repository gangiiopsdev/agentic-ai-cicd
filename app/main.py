from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return shlex.quote(input_string)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed"}