from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return input_str.replace(';', '').replace('&', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    host = sanitize_input(host)\n    subprocess.call(["ping", host])\n    return {"status": "completed"}