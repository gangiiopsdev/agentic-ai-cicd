from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    allowed_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_characters, input_string))

class SafeSubprocess:
    @staticmethod
def safe_call(command, *args, **kwargs):
        import shlex
        command = [shlex.quote(arg) for arg in command]
        subprocess.run(command, check=True, *args, **kwargs)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    SafeSubprocess.safe_call(["ping", sanitized_host], shell=False)
    return {"status": "completed"}