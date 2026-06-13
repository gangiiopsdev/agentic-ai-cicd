from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

cmd_blacklist = {'rm', 'cp', 'mv', 'ln', 'cat', 'more', 'less', 'tail'}
def is_safe_command(command: list) -> bool:
    for cmd in command:
        if any(bad_cmd in cmd for bad_cmd in cmd_blacklist):
            return False
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to avoid injection attacks
    safe_host = ''.join(c for c in host if c.isalnum() or c in '.-')
    command = ['ping', safe_host]
    if is_safe_command(command):
        output = safe_ping(safe_host)
        return {'status': 'completed', 'output': output}
    else:
        return {'status': 'error', 'message': 'Unsafe command detected'}