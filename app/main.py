from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Implement input sanitization logic here
    return input_string.strip()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "message": "Ping successful"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "message": str(e.output)}