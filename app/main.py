from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safer implementation using subprocess.run for better control and security
    result = subprocess.run([quote('ping'), quote(sanitized_host)], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}