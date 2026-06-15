from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ' '.join([x for x in input_string.split() if x.isalnum()])

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}