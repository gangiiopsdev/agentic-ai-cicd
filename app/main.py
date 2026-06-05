from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '')

class Sanitize:
    @staticmethod
def clean_input(input_str):
        sanitized = ''.join(ch for ch in input_str if ch.isalnum() or ch.isspace())
        return sanitized

global_escape_shell_arg = lambda x: escape_shell_arg(x)

global_clean_input = lambda x: Sanitize.clean_input(x)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input before using subprocess
    host = global_clean_input(host)
    subprocess.run(['ping', global_escape_shell_arg(host)], check=True, capture_output=True, text=True)
    return {'status': 'completed'}