from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(filter(lambda x: x.isalnum() or x in '.', input_str))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host != host:
        raise ValueError("Invalid characters detected in hostname")
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}