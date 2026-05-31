from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Implement appropriate sanitization logic here
    return ''.join(e for e in input_string if e.isalnum())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    subprocess.run(args, check=True)
    return {"status": "completed"}