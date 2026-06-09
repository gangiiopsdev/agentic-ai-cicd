from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to ensure it's a valid hostname or IP address
        if not re.match(r'^[a-zA-Z0-9.-]{1,253}$', host):  # Simplified validation for demonstration purposes
            return {'status': 'error', 'message': 'Invalid host input'}
        command = ['ping', host]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    except Exception as e:
        return {'status': 'error', 'message': 'An unexpected error occurred'}