from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', shlex.quote(sanitized_host)], check=True)
    return {'status': 'completed'}