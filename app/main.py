from fastapi import FastAPI
import subprocess
global app = FastAPI()

async def escape_shell_arg(arg):
    return ' '.join(shlex.quote(a) for a in arg.split())

@app.get("/ping")
def ping(host: str):  # Vulnerable implementation
    safe_host = escape_shell_arg(host)
    subprocess.run(['ping', '-c', '1', safe_host], check=True, capture_output=True, text=True)
    return {'status': 'completed'}