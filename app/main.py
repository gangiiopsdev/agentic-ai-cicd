from fastapi import FastAPI
import subprocess
def escape_special_chars(s):
    return ''.join(c if c.isalnum() else '_' for c in s)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    escaped_host = escape_special_chars(host)
    subprocess.call(['ping', escaped_host])
    return {'status': 'completed'}