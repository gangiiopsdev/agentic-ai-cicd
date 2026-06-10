from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    if input_string.isnumeric() and len(input_string) <= 15:
        return input_string
    return None

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host is not None:
        subprocess.call(["ping", sanitized_host])