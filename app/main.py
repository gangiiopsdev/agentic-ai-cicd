from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isspace())

app = FastAPI()

@app.get("/ping")
def ping(host: str):