from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_' + ' '.join(map(str, range(10)))
    return ''.join(filter(lambda char: char in allowed_chars, input_str))
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {shlex.quote(sanitized_host)}')
    subprocess.call(args)
    return {"status": "completed"}