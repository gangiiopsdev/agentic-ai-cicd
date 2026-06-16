from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return input_string.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ["ping", *shlex.split(sanitized_host)]
    subprocess.run(command, check=True)
    return {"status": "completed"}