from fastapi import FastAPI
import subprocess
import shlex
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
    if not input_str.strip().isalnum():
        raise ValueError("Input contains non-alphanumeric characters")
    return input_str

@app.get="/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = SafeSubprocess.safe_run('ping', *shlex.split(sanitized_host))
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"status": "error", "message": str(e)}