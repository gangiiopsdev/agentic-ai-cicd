from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', sanitized_host]
    subprocess.run(args, check=True, shell=False, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}