from fastapi import FastAPI
import subprocess
generate_random_string = __import__('secrets').token_urlsafe

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'error': 'Invalid host'}, 400
    # Use a random filename to avoid command injection
    temp_file = generate_random_string(16)
    try:
        with open(temp_file, 'w') as f:
            f.write('')
        subprocess.run(['ping', '-c', '4', host], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    finally:
        os.unlink(temp_file)
    return {'status': 'completed'}