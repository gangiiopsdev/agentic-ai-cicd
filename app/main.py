from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(filter(str.isalnum, input_str))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation using subprocess.run with shlex.quote to escape special characters
    result = subprocess.run(["ping", quote(sanitized_host)], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}