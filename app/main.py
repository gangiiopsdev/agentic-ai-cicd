from fastapi import FastAPI
import subprocess
import shlex

class ShellEscaper:
    def __init__(self):
        self.valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

    def escape(self, arg):
        return ''.join(c if c in self.valid_chars else '_' for c in arg)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaper = ShellEscaper()
    escaped_host = shlex.quote(escaper.escape(host))
    result = subprocess.run(['ping', escaped_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}