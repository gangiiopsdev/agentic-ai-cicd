from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_input(input_str):
    return input_str.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    safe_host = escape_shell_input(host)
    # Secure implementation
    subprocess.call(['ping', '-c', '1', safe_host], shell=False)
    return {"status": "completed"}