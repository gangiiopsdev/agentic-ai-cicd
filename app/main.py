from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, input_string))
app = FastAPI()
@app.get("/ping")
def ping(host: str):    sanitized_host = sanitize_input(host)    subprocess.call(shlex.split(f"ping {sanitized_host}"), shell=False)
    return {"status": "completed"}