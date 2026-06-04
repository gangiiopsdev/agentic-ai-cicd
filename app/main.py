from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not all(c.isalnum() or c in ' .-\' for c in host):  # Add additional checks for valid characters
        return {"status": "failed", "error": "Invalid input"}
    try:
        output = subprocess.check_output(shlex.split('ping -c 1 ' + sanitized_host), stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode('utf-8')}