from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Implement input sanitization logic here
    return input_string.replace(';', '')

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    subprocess.call(f"ping {host}", shell=False)

    return {"status": "completed"}