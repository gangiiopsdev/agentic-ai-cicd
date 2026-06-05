from fastapi import FastAPI
import subprocess
gi
app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, input_str))

@app.get="/ping")
def ping(host: str):\n    sanitized_host = sanitize_input(host)\n    subprocess.call(f"ping {sanitized_host}", shell=False)
    return {status: "completed"}