from fastapi import FastAPI
import subprocess
from sanic.response import json
def sanitize_input(input_str):
    # Implement your sanitization logic here, e.g., using regex or whitelisting
    return input_str

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    subprocess.run(["ping", host], check=True, shell=False)
    return json({"status": "completed"})