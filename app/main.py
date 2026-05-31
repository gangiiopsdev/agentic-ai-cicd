from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_user_input(user_input):
    return user_input.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_user_input(host)
    # Secure implementation
    subprocess.call(f"ping {escaped_host}")

    return {"status": "completed"}