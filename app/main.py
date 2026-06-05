from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input):
    return ''.join(filter(str.isalnum, input))

@app.get="/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safe implementation
    subprocess.call(['ping', sanitized_host], shell=False)
    return {"status": "completed"}