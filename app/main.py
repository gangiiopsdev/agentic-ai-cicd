from fastapi import FastAPI
import subprocess
import shlex
def run_safe_ping(host: str):
    try:
        # Sanitize input using regular expressions or other methods
        sanitized_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
        command = ['ping', sanitized_host]
        command_str = ' '.join(shlex.quote(arg) for arg in command)
        subprocess.run(command_str, shell=True, timeout=5, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        return {'error': str(e)}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return run_safe_ping(host)