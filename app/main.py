from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

@app.get("/ping")
def ping(host: str):
    sanitized_host = quote(sanitize_input(host))
    subprocess.run(['ping', '-c', '1', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}