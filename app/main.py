from fastapi import FastAPI
import subprocess
import shlex

def validate_and_quote_host(host):
    if not all(c.isalnum() for c in host):
        raise ValueError("Invalid input")
    return shlex.quote(host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):