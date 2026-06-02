from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(input_string):
    # Simple sanitization example: allow only alphanumeric characters and a few special characters
    return ''.join(c for c in input_string if c.isalnum() or c in ['-', '.', ' ', '_', ':', '@'])

@app.get("/ping")
def ping(host: str):