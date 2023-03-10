import os
import argparse
import requests
import time

parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, required=True, help='Port number to test')
parser.add_argument('--status-code', type=int, required=False, help='Expected HTTP status code', default=200)
args = parser.parse_args()

url_to_test = 'http://localhost' + ':' + str(args.port)
expected_code = args.status_code

def test_microservice(url: str, expected_status_code: int):
    retries = 0
    max_retries = 30
    while True:
        try:
            response = requests.get(url)
            if response.status_code == expected_status_code:
                print(f'Microservice returned {response.status_code}')
                break
            else:
                raise Exception(f'Unexpected status code. Got {response.status_code}')
        except requests.exceptions.RequestException as e:
            retries += 1
            if retries > max_retries:
                raise e
            print(f'Microservice failed with error: {e}. Retrying in 5 seconds.')
            time.sleep(5)

if __name__ == '__main__':
    test_microservice(url_to_test, expected_code)
