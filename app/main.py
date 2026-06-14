from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(c in allowed_chars for c in host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):