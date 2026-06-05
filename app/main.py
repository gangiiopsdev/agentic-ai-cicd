from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.Popen with shell=False and check=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

@app.get("/ping")
def ping_route(host: str):
    try:
        # Validate the input to ensure it only contains allowed characters
        if not all(c.isalnum() or c in '.-' for c in host):
            raise ValueError('Invalid hostname')
        result = ping(host)
        return {'status': 'completed', 'output': result}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}