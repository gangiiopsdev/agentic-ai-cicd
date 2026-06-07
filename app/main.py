from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Use subprocess.run for safer execution without shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it does not contain malicious content
    if any(char in host for char in ["&&", ";", "||", "|"]):  # Improved validation
        raise ValueError("Invalid input")
    response = safe_ping(host)
    return {"status": "completed", "response": response}