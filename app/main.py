from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_input(input):
    return input.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}