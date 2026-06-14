from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_input(input_str):
    return input_str.replace(';', '').replace('&', '').replace('|', '').replace('^', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_input(host)
    subprocess.run(f"ping {escaped_host}", shell=False, check=True)
    return {"status": "completed"}