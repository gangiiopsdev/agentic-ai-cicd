from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, host))
app = FastAPI()
@app.get("/ping")
def ping(host: str):  
    sanitized_host = shlex.quote(sanitize_input(host))
    subprocess.run(["ping", "-c", "1", sanitized_host], shell=False)
    return {"status": "completed"}