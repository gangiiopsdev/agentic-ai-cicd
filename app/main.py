from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    # Implement input sanitization logic here
    return ''.join(filter(str.isalnum, input_str))

app = FastAPI()

@app.get("/ping")
def ping(host: str):  # Ensure host is sanitized before use
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode('utf-8')}\n