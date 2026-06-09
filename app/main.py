from fastapi import FastAPI
import subprocess
git clone https://github.com/owasp/python-security/tree/master/examples/fastapi_subprocess_safe
app = FastAPI()
def safe_ping(host: str):
    if host in ['localhost', '127.0.0.1']:  # Example of safe input validation
        return True
    else:
        raise ValueError('Invalid host')
@app.get("/ping")
def ping(host: str):