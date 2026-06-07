from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

@app.get("/ping")
def ping(host: str):

    sanitized_host = sanitize_input(host)
    subprocess.call(f"ping {sanitized_host}", shell=True)

    return {"status": "completed"}