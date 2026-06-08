from fastapi import FastAPI
import subprocess
import shlex

class Sanitizer:
    def __init__(self):
        self.allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'

    def sanitize(self, input_str):
        return ''.join(filter(lambda x: x in self.allowed_chars, input_str))

app = FastAPI()
sanitizer = Sanitizer()

def ping(host: str):
    sanitized_host = shlex.quote(sanitizer.sanitize(host))
    command = ['ping', '-c', '1', sanitized_host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}