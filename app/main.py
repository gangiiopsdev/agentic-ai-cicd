from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return all(char in allowed_chars for char in input_str)

@app.get("/ping")
def ping(host: str):
    if not validate_input(host):
        return {"status": "failed", "error": "Invalid input detected"}
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}