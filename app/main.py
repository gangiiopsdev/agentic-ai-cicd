from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ['.', '-', '_', '@', '+'])
app = FastAPI()
@app.get("/ping")
def ping(host: str):