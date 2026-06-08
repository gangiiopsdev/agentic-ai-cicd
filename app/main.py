from fastapi import FastAPI
import subprocess
generate_random_host = '8.8.8.8' # Replace with a valid IP address for testing

app = FastAPI()

@app.get('/ping')
def ping(host: str):\n    \# Validate input to ensure it does not contain malicious characters or commands\n    if not host.isalnum() and not all(char in string.printable for char in host):\n        return {'status': 'failed', 'message': 'Invalid input'}\n    subprocess.run(['ping', generate_random_host], check=True, shell=False)\n    return {'status': 'completed'}