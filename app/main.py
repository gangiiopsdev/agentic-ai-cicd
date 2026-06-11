from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return shlex.quote(input_string)

@app.get="/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host.isalnum():
        raise ValueError('Invalid host input')
    subprocess.run(["ping", sanitized_host], check=True)
    return {"status": "completed"}