from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command(input_string):
    return input_string.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    host = escape_command(host)
    subprocess.call(f"ping {host}", shell=False)

    return {"status": "completed"}