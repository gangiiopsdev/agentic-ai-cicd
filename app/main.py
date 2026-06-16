from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command: list[str]):
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {e.returncode}, Output: {e.output}'

global run_subprocess
run_subprocess = SafeSubprocess.run

app = FastAPI()
def sanitize_input(input_string):
    # Implement input sanitization logic here
    return ''.join(filter(str.isalnum, input_string))
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    result = run_subprocess(['ping', sanitized_host])
    return {'status': 'completed', 'result': result}