from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=False)
    return {'output': result.stdout}