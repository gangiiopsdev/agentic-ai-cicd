from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    if not input_string.isalnum():
        raise ValueError("Invalid input")

@app.get="/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        subprocess.call(["ping", sanitized_host], check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}