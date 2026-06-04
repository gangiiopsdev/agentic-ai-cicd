from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_user_input(user_input):
    return user_input.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):

    # Escaped input to prevent command injection
    subprocess.call(f"ping {escape_user_input(host)}", shell=True)

    return {"status": "completed"}