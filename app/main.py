from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    # Use subprocess.run instead of subprocess.call and avoid shell=True for security reasons.
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Secure implementation using execute_ping function.
    response = execute_ping(host)
    return {"status": "completed", "response": response}