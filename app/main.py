from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ['.', '-', '_'])

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    # Use subprocess.run instead of subprocess.call and avoid shell=True
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}