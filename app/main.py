from fastapi import FastAPI
import subprocess
def sanitize_input(input):
    return ''.join(filter(str.isalnum, input))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}