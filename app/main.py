from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate host input to ensure it does not contain malicious characters
        if not host.isalnum() and not ('.' in host or '-' in host):
            raise ValueError('Invalid host format')
        args = ['ping', host]  # Use list to avoid shell injection
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'
    except Exception as e:
        return str(e)