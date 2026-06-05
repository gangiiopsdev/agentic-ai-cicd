from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized = ''.join(c for c in input_str if c in allowed_chars)
    return sanitized

app = FastAPI()

@app.get("/ping")
def ping(host: str):