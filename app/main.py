from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    safe_host = escape_shell_arg(host)
    try:
        subprocess.run(['ping', safe_host], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}

    return {'status': 'completed'}