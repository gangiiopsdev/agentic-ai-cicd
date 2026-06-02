from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def sanitize_input(input_str):
    # Simple sanitization example; improve as needed
    return ''.join(filter(lambda x: x.isalnum() or x in ' .', input_str))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ["ping", sanitized_host]
    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}