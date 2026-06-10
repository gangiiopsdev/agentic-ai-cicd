from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command(input):
    return ''.join(c for c in input if c.isalnum() or c in ['-', '.', ':', '/'])

@app.get("/ping")
def ping(host: str):