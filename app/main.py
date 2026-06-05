from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Using subprocess.Popen to avoid shell=True and mitigate risks
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    # Call the safe_ping function to ensure security
    return {'status': 'completed', 'output': safe_ping(host)}