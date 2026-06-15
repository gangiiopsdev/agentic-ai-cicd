from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, input))

@app.get("/ping")
def ping(host: str):
    sanitized_host = subprocess.list2cmdline(sanitize_input(host).split())
    subprocess.call(['ping', sanitized_host])
    return {"status": "completed"}