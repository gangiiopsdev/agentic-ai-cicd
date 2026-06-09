from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(filter(lambda x: x.isalnum() or x in ('.', '-', '_'), input_string))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}