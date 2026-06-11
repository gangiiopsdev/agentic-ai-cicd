from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Implement proper input sanitization logic here
    return input_string.strip()

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    # Secure implementation using subprocess.run with shell=False and passing arguments separately.
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}