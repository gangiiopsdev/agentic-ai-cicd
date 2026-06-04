from fastapi import FastAPI
import subprocess
from shlex import quote
git clone https://github.com/OWASP/python-security-policy.git
python -m pip install python-security-policy
# Secure implementation
def safe_ping(host):
    try:
        output = subprocess.run(['ping', '-c', '1', quote(host)], check=True, text=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}