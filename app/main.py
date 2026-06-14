from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    # Add your sanitization logic here
    return user_input.strip()

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    try:
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}