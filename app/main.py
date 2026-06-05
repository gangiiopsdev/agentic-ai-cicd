from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use check_output to avoid shell=True and improve security
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e.output)}

# Preventive Controls:
# 1. Input Validation: Validate and sanitize the input to ensure it does not contain malicious content.
# 2. Access Control: Restrict access to the /ping endpoint to authorized users only.
# 3. Logging: Implement detailed logging for all requests made through the ping endpoint.