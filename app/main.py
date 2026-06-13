from fastapi import FastAPI
import subprocess
from shlex import quote
from os.path import abspath, join

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ['-', '.', '_'])

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = quote(sanitize_input(host))
        result = subprocess.run([abspath(join('/', 'bin', 'ping')), sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}