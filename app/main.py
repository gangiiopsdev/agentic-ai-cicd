from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    # Add your input sanitization logic here
    return ''.join(c for c in input_string if c.isalnum() or c in [',', '-', '.'])

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', shlex.quote(sanitized_host)]
    subprocess.run(args, check=True)
    return {"status": "completed"}