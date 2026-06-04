from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_user_input(user_input):
    return user_input.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    safe_host = escape_user_input(host)
    # Secure implementation using subprocess.run with shell=False and args parameter
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}