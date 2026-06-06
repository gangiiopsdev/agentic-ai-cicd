from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(user_input):
    return ''.join(e for e in user_input if e.isalnum() or e in ('-', '.', '_', '@'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = quote(sanitize_input(host))
    # Use a safer method to execute the command, such as using os.system with proper quoting
    subprocess.run(f'"ping" "{sanitized_host}"', check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    return {"status": "completed"}