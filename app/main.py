from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def sanitize_input(input_str):
    # Simple sanitization example; improve as needed
    return input_str.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ["ping", sanitized_host]
    subprocess.call(command, shell=False)
    return {"status": "completed"}