from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell(input_str):
    return input_str.replace(';', '').replace('&', '').replace('|', '')

@app.get="/ping")
def ping(host: str):

    # Safe implementation
    safe_host = escape_shell(host)
    subprocess.call(['ping', safe_host])

    return {"status": "completed"}