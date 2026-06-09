from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    allowed_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_characters, input_string))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(["ping", sanitized_host], shell=False)
    return {"status": "completed"}