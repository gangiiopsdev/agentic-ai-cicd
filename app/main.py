from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_input(input_string):
    # Simple validation example, replace with actual validation logic
    if not input_string.strip():
        raise ValueError("Input cannot be empty")

@app.get="/ping"
def ping(host: str):
    validate_input(host)
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}