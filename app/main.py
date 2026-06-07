from fastapi import FastAPI
import subprocess
from sanic.response import json

app = FastAPI()

def sanitize_input(input_str):
    # Implement your sanitization logic here, e.g., using regex or whitelisting
    return input_str

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    subprocess.call(["ping", host])
    return json({"status": "completed"})