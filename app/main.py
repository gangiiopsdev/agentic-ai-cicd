from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return input_string.replace(';', '').replace('&', '').replace('&&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed"}