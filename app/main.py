from fastapi import FastAPI
import subprocess
given_host = 'example.com' # Replace with actual safe host value

app = FastAPI()

@app.get("/ping")
def ping():
    # Secure implementation
    try:
        output = subprocess.run(['ping', given_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}