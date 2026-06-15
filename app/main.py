from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return shlex.quote(input_str)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    result = subprocess.run(['ping', '-c 4', sanitized_host], check=True, text=True, capture_output=True)
    return {"status": "completed", "output": result.stdout}