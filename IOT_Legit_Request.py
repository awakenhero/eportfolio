import requests  # for posting  HTTP requests this library requires ( Manual installation required via pip)
import time     # for adding delays this library requires 

def send_request(url, client_id): 
    # Send a request to apache2 server
    # This function simulates an IoT device sending data to a apache2 server
    try: 
        #  Posting http request to get response  from apache2 server
        # This URL should be the endpoint where the IoT device sends data
        resp = requests.get(url)
        print(f"Device {client_id} -> Status: {resp.status_code}, URL: {url}") #  Logging the response with status code and IP or URL
        
    except requests.exceptions.RequestException as e:
        # Logging error when apache2 server  fail to process the request
        print(f"Device {client_id} failed: {e}") 

# Test server URL where apache2 is running on KALI Linux
SERVER_URL = 'http://192.168.65.2/'

# Simulate a few IoT devices
NUM_DEVICES = 10 # Number of devices for  simulating requests
DELAY = 2  # Delay between the http requests. this is to avoid DDOS attack. 

# Send test requests
for device in range(1, NUM_DEVICES + 1): # this loop to simulate 10 IOT devices
    send_request(SERVER_URL, device) # senting request to apache2 server
    time.sleep(DELAY)  # delay between the http requests. this is to avoid DDOS attack. 


    """
References:


HTTP Requests: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request 
Time Delay:    https://docs.python.org/3/library/time.html
Sending HTTP Requests: https://realpython.com/python-requests/
Function define: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
Error Handling: https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions
Constants used for Server URL: https://peps.python.org/pep-0008/#constants
integer declaration for simulating IOT devices : https://docs.python.org/3/reference/lexical_analysis.html#integer-literals
Forloop with range function: https://docs.python.org/3/tutorial/controlflow.html#for-statements
Time delay for legitimate requests: https://docs.python.org/3/library/time.html#time.sleep

"""