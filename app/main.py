from fastapi import FastAPI
import subprocess
import shlex
class CommandSanitizer:
    def sanitize(self, command: str) -> list:
        try:
            return shlex.split(command)
        except ValueError as e:
            raise ValueError(f'Invalid command format: {e}')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitizer = CommandSanitizer()
    args = sanitizer.sanitize('ping ' + host)
    subprocess.run(args, check=True)
    return {'status': 'completed'}