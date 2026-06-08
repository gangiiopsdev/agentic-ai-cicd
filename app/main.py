from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    if not input_str.isalnum():
        raise ValueError('Invalid input')
    return input_str

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}