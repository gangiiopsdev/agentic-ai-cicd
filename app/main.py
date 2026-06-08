from fastapi import FastAPI
import subprocess
def is_safe_hostname(hostname):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_' if hostname.startswith('[') else 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in hostname)

app = FastAPI()

def safe_subprocess(command, *args):
    import shlex
    full_command = [shlex.quote(arg) for arg in command]
    subprocess.run(full_command + list(args), check=True)

@app.get('/ping')
def ping(host: str):
    if is_safe_hostname(host) and ':' not in host:
        safe_subprocess(['ping', '-c', '1'], host)
    else:
        raise ValueError('Invalid hostname')
    return {'status': 'completed'}