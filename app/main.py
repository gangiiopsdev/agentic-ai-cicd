from fastapi import FastAPI
import shlex

class CommandSanitizer:
    def __init__(self, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'):
        self.allowed_chars = allowed_chars

    def sanitize(self, string):
        return ''.join(c for c in string if c in self.allowed_chars)

app = FastAPI()
sanitizer = CommandSanitizer()

@app.get("/ping")
def ping(host: str):
    parts = shlex.split(host)
    sanitized_parts = [sanitizer.sanitize(part) for part in parts]
    command = ' '.join(sanitized_parts)
    result = subprocess.run(command, capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}