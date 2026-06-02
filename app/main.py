from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_input(host)
    subprocess.call(['ping', quote(safe_host)], shell=False)
    return {"status": "completed"}