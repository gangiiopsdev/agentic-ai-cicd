from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-:_@')
    return ''.join(c for c in input_str if c in allowed_chars)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.check_output(['ping', '-c', '1', sanitized_host], shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": e.output.decode()}
    return {"status": "completed", "output": output.decode()}