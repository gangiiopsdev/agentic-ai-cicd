from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_input(host: str) -> bool:
    return host.isalnum()

@app.get="/ping")
def ping(host: str):
    if not validate_input(host):
        return {"error": "Invalid input"}, 400

    # Use subprocess.run with shell=False and proper argument handling
    subprocess.run(["ping", host], check=True)

    return {"status": "completed"}