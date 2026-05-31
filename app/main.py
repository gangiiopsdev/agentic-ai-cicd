from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    if not input_str.isalnum():
        raise ValueError("Input contains non-alphanumeric characters")
    return input_str

@app.get="/ping")
def ping(host: str):    host = sanitize_input(host)
    subprocess.call(["ping", host])

return {"status": "completed"}