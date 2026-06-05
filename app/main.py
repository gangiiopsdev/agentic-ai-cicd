from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e.isspace())

@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_input(host)
    subprocess.call(["ping", '-c', '1', safe_host])  # Use '-c' to limit the number of pings
    return {"status": "completed"}