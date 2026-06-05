from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Implement proper input sanitization here
    pass

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host:
        subprocess.call(['ping', sanitized_host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid input"}