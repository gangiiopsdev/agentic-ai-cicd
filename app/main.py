from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(value: str) -> str:
    if not value.strip() or not all(c.isalnum() or c in ['.', '-'] for c in value):
        raise ValueError('Invalid input')

app = FastAPI()

@app.get('/ping')
def ping(host: str):