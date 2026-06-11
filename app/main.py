from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    @staticmethod
def sanitize_input(input_string):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        return ''.join(char for char in input_string if char in allowed_chars)

    @staticmethod
def run_ping(host: str):
        sanitized_host = PingService.sanitize_input(host)
        command_parts = ['ping', sanitized_host]
        command_str = ' '.join(shlex.quote(part) for part in command_parts)
        subprocess.run(command_str, check=True, shell=False)

app = FastAPI()

class PingEndpoint:
    @staticmethod
def ping(host: str):
        PingService.run_ping(host)
        return {"status": "completed"}