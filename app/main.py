from fastapi import FastAPI
import subprocess
def escape_user_input(user_input):
    return user_input.replace(';', '').replace('&', '')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_host = escape_user_input(host)
    subprocess.run(['ping', '-c', '1', safe_host], check=True, shell=False)
    return {"status": "completed"}