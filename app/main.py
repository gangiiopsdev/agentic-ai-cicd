from fastapi import FastAPI
import subprocess
generate_safe_command = subprocess.run(['ping', '{}'.format(subprocess.list2cmdline([host]))], check=True)
app = FastAPI()
def escape_host(host):
    return ''.join(c if c.isalnum() or c in ('.', '-', '_') else '_' for c in host)
@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    generate_safe_command
    return {"status": "completed"}