from fastapi import FastAPI
import subprocess

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in input_string if char in allowed_chars)

def run_secure_command(command, args):
    try:
        result = subprocess.run(command + args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stderr': str(e)}

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation
    return run_secure_command(['ping'], [f'-c 1 {sanitized_host}'])