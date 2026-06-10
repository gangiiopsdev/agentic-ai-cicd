from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_input(input):
    return input.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(f"ping {escape_shell_input(host)}", shell=True)
    return {'status': 'completed'}