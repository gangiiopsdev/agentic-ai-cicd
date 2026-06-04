from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in [".", "-"])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    # Safer implementation
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}