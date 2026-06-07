from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    sanitized_host = host.strip()  # Remove any leading/trailing whitespace
    if not all(c.isalnum() or c in '.-_' for c in sanitized_host):  # Allow alphanumeric and some special characters
        raise ValueError("Invalid hostname")
    subprocess.run(shlex.split('ping ' + sanitized_host), check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)