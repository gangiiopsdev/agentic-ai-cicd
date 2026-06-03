from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def sanitize_input(user_input):
    return ''.join(e for e in user_input if e.isalnum() or e in ['.', '-', '_'])

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation
    subprocess.call([os.path.abspath('ping'), sanitized_host])
    return {"status": "completed"}