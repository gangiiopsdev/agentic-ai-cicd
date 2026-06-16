from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Implement your sanitization logic here
    return ''.join(filter(lambda char: char.isalnum() or char in ['.', '-', '_', ' ', '/', ':'], input_string))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], check=True, shell=False)
    return {"status": "completed"}