from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Implement proper input sanitization logic here
    return ''.join(filter(str.isalnum, input_string))

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    subprocess.call(f"ping {host}")
    return {"status": "completed"}