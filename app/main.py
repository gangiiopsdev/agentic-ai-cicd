from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input):
    return ''.join(filter(str.isalnum, input))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation
    args = ['ping', sanitized_host]
    subprocess.run(args, check=True)

    return {"status": "completed"}