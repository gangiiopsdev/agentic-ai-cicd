from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Implement input validation and sanitization logic here
    return subprocess.quote(input_string)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}