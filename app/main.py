from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return input_str.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    host = sanitize_input(host)
    subprocess.call(["ping", host])
    return {"status": "completed"}