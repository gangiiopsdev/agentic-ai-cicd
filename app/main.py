from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def validate_input(input_string):
    if not all(c.isalnum() or c in '.-_' for c in input_string):
        raise ValueError("Invalid input")

@app.get="/ping")
def ping(host: str):
    validate_input(host)
    subprocess.call(["ping", host], shell=False)  # Adding shell=False to prevent command injection
    return {"status": "completed"}