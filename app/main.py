from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.check_output(shlex.split(f'ping -c 1 {shlex.quote(sanitized_host)}'), stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode('utf-8')}\nimport ast
import re
def safe_eval(code):
    tree = ast.parse(code, mode='eval')
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp) or isinstance(node, ast.UnaryOp):
            return None
    return eval(code)
@app.get("/ping_safe")
def ping_safe(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.check_output(safe_eval(f'"ping -c 1 {sanitized_host}"'), stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode('utf-8')}\n