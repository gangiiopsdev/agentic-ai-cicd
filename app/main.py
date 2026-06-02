from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_run(command, *args):
        try:
            result = subprocess.run([command] + [shlex.quote(arg) for arg in args], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode()
        except subprocess.CalledProcessError as e:
            raise Exception(f"Command failed with error: {e.stderr.decode()}")

app = FastAPI()
def sanitize_input(input_str):
    if not input_str.isalnum():
        raise ValueError("Input contains non-alphanumeric characters")
    return input_str

def validate_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']  # Example allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    validate_host(sanitized_host)
    output = SafeSubprocess.safe_run('ping', sanitized_host)
    return {"status": "completed", "output": output}