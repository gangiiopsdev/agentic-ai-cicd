from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    # Add your input sanitization logic here
    return ''.join(c for c in input_string if c.isalnum() or c in [',', '-', '.'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', shlex.quote(sanitized_host)]
    # Use check_output instead of run to capture output
    result = subprocess.check_output(args, stderr=subprocess.STDOUT, text=True)
    return {"status": "completed", "output": result}