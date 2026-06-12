from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    return ''.join(filter(lambda x: x.isalnum() or x in '._', user_input))

@app.get("/ping")
def ping(host: str):

    sanitized_host = sanitize_input(host)
    subprocess.call(f"ping {sanitized_host}", shell=True)

    return {"status": "completed"}