from fastapi import FastAPI
import subprocess
def escape_user_input(user_input):
    return user_input.replace(';', '').replace('&', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = escape_user_input(host)
    # Secure implementation
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}