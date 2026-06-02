from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e.isspace())
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(shlex.split(f"ping {sanitized_host}", posix=True), check=True, capture_output=True, text=True)
    return {"status": "completed"}