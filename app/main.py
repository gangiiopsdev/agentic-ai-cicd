from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    # Implement proper sanitization logic here
    return ''.join(char for char in input_string if char.isalnum())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}