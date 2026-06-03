from fastapi import FastAPI
import subprocess
import shlex

class InputSanitizer:
    @staticmethod
def sanitize_input(input_str):
        return ''.join(filter(str.isalnum, input_str))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = InputSanitizer.sanitize_input(host)
        # Use shlex.quote to safely include the host in the command line
        result = subprocess.run(['ping', shlex.quote(sanitized_host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}