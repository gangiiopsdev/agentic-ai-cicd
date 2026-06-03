from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host):
    return ''.join(char for char in host if char.isalnum() or char in ['-', '.', '_', ':'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):