from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda char: char in allowed_chars, host))

@app.get("/ping")
def ping(host: str):
    validated_host = validate_host(host)
    if not all(c.isalnum() or c in '-.' for c in validated_host):
        raise ValueError("Invalid host name")
    command = ['ping', '-c', '1', validated_host]
    subprocess.run(command, check=True, shell=False)
    return {"status": "completed"}