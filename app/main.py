from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    # Implement your sanitization logic here
    return input_string.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str): 
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], shell=False, check=True)

    return {"status": "completed"}