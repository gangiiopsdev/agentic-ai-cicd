from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_input(value: str) -> bool:
    return all(c.isalnum() for c in value)

@app.get("/ping")
def ping(host: str):
    if not safe_input(host):  # Check for alphanumeric characters only
        return {"error": "Invalid input"}
    # Use subprocess.run instead of subprocess.call
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}