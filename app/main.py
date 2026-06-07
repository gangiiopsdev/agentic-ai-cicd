from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    # Implement input sanitization logic here
    return input_string.replace(';', '')

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    command = shlex.split(f"ping {host}")
    subprocess.call(command, shell=False)

    return {"status": "completed"}