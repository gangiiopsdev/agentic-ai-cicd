from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return input_str.replace(';', '').replace('&', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation
    try:
        subprocess.run(['ping', '-c 1', sanitized_host], check=True, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}