from fastapi import FastAPI
import subprocess
import shlex

class Sanitizer:
    @staticmethod
def sanitize_input(input_string):
        # Using shlex.quote for better sanitization
        return shlex.quote(input_string)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    sanitized_host = Sanitizer.sanitize_input(host)
    # Using subprocess.run with shell=False and passing arguments separately
    subprocess.run(["ping", sanitized_host], check=True, capture_output=True)
    return {"status": "completed"}