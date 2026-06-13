from fastapi import FastAPI
import subprocess
c
app = FastAPI()

def sanitize_input(input_string):
    # Implement input sanitization logic here
    return input_string.strip()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        output = e.output
    return {"status": "completed", "output": output.decode()}