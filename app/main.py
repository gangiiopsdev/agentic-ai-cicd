from fastapi import FastAPI
import subprocess
def escape_shell_argument(arg):
    return arg.replace('`', '`\x60').replace('$', '\x24').replace('\', '\\\\')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_argument(host)
    subprocess.run(['/usr/bin/ping', f'-c 1 {escaped_host}'], check=True, capture_output=True, text=True)
    return {"status": "completed"}