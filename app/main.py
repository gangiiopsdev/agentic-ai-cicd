from fastapi import FastAPI
import subprocess

class ShellEscape:
    @staticmethod
def escape_shell_arg(arg: str) -> str:
        if not isinstance(arg, str):
            return arg
        if ' ' in arg or '	' in arg or '&' in arg or ';' in arg or '|' in arg or '>' in arg or '<' in arg:
            return f'"{arg}"'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = ShellEscape.escape_shell_arg(host)
    subprocess.call(['ping', safe_host], shell=False, executable=None)
    return {"status": "completed"}