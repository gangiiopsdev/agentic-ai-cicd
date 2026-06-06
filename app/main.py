from fastapi import FastAPI
import re

def escape_host(host):
    # Use regex to replace special characters that could be used for command injection
    return re.sub(r'[;&]', '', host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    # Use subprocess.run to avoid shell=True and improve security
    result = subprocess.run(['ping', '-c', '1', escaped_host], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}