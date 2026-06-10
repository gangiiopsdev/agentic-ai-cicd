from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Using subprocess.Popen instead of subprocess.call for better control
        result = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = result.communicate()
        return output.decode('utf-8')
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}