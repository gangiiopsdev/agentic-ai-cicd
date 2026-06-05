from fastapi import FastAPI
import subprocess
import shlex

def escape_shell_arg(arg):
    return shlex.quote(arg)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with proper shell argument escaping
    try:
        output = subprocess.run(['ping', escape_shell_arg(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}