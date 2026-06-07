from fastapi import FastAPI
import subprocess
from shlex import quote
from subprocess import Popen, PIPE

app = FastAPI()

def sanitize_input(input_str):
    return quote(input_str)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    result = Popen(["ping", sanitized_host], stdout=PIPE, stderr=PIPE)
    output, error = result.communicate()
    return {"status": "completed", "output": output.decode(), "error": error.decode() if error else None}