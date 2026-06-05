from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '')

class Sanitize:
    @staticmethod
def clean_input(input_str):
        sanitized = ''.join(ch for ch in input_str if ch.isalnum() or ch.isspace())
        return sanitized

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input before using subprocess
    host = Sanitize.clean_input(host)
    result = subprocess.run(['ping', escape_shell_arg(host)], check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}