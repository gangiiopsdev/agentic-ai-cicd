from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safer implementation using subprocess.run for better control and security
    result = subprocess.run(['ping', '-c 1', sanitized_host], capture_output=True, text=True, check=True, shell=False)
    return {"status": "completed", "output": result.stdout}