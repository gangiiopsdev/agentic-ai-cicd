from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_input(value: str) -> bool:
    return all(c.isalnum() for c in value)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not safe_input(host):  # Check for alphanumeric characters only
        return {"error": "Invalid input"}
    subprocess.call(["ping", host])
    return {"status": "completed"}