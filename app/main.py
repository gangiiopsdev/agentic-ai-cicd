from fastapi import FastAPI
import subprocess
class ShellEscapeException(Exception):
    pass
def shell_escape(input_str: str) -> str:
    if '&&' in input_str or ';' in input_str or '|' in input_str or '`' in input_str or '"' in input_str or "'" in input_str or '\' in input_str or '<' in input_str or '>' in input_str or '(' in input_str or ')' in input_str or '[' in input_str or ']' in input_str:
        raise ShellEscapeException("Shell escape detected")
    return input_str
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        shell_escaped_host = shell_escape(host)
        subprocess.call(['ping', '-c 1', shell_escaped_host])
    except ShellEscapeException as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed"}
def is_valid_host(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts