from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return input_string.replace(';', '').replace('&', '').replace('&&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(f"ping {sanitized_host}", shell=False)
    return {"status": "completed"}