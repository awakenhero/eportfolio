import requests  # for posting  HTTP requests this library requires ( Manual installation required)
import time     # for adding delays this libray requires 

def send_request(url, client_id):
    # Send a request to apache 2 server
    # This function simulates an IoT device sending data to a apaceh 2 server
    try:
        #  Posting http request t to get response  from apache 2 server
        # This URL should be the endpoint where the IoT device sends data
        resp = requests.get(url)
        print(f"Device {client_id} -> Status: {resp.status_code}, URL: {url}")
        
    except requests.exceptions.RequestException as e:
        # Logging error when apache 2 server  fail to process the request
        print(f"Device {client_id} failed: {e}")

# Test server URL where apache2 is running on KALI Linux
SERVER_URL = 'http://192.168.65.2/'

# Simulate a few IoT devices
NUM_DEVICES = 10
DELAY = 2  # Delay between the http requests. this is to avoid DDOS attack. 

# Send test requests
for device in range(1, NUM_DEVICES + 1):
    send_request(SERVER_URL, device)
    time.sleep(DELAY)  # delay between the http requests. this is to avoid DDOS attack. 


    """
References:


HTTP Requests: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request 
Time Delay:    https://docs.python.org/3/library/time.html
Sending HTTP Requests: https://realpython.com/python-requests/
Function define: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
Error Handling: https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions
Constants used foe Server URL: https://peps.python.org/pep-0008/#constants
integer declaration for simulatng IOT devices : https://docs.python.org/3/reference/lexical_analysis.html#integer-literals
Forloop with range function: https://docs.python.org/3/tutorial/controlflow.html#for-statements
Time delay for legitimate requests: https://docs.python.org/3/library/time.html#time.sleep

"""