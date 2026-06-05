from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return input_str.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    # Safer implementation
    subprocess.call(['ping', host])
    return {"status": "completed"}