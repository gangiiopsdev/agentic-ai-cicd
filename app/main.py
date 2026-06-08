from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate input to ensure it does not contain shell metacharacters
        if any(char in host for char in "$&;()|<>\`'"*?[]{}$&;()|<>\`'"*?[]{}
{!@#$%^&*()_+-=}{[]|:;'<>,.?/~`"
):
            raise ValueError('Invalid input')
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}