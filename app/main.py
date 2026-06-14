from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_string if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = subprocess.list2cmdline(["ping", sanitized_host])
    subprocess.call(sanitized_host, shell=False)
    return {"status": "completed"}