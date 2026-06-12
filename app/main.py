from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Implement your sanitization logic here
    return input_string.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(["ping", sanitized_host])

    return {"status": "completed"}