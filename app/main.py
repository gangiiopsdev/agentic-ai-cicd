from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_shell_arg(arg):
    return shlex.quote(arg)

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host input to ensure it does not contain malicious content
        if 'ping' in host or ';' in host:
            raise ValueError('Invalid input')
        result = subprocess.run(["ping", escape_shell_arg(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e.stderr.decode())}