import requests

# TODO: Change this to the Radmin IP of your Cloud PC!
RADMIN_IP = "26.65.113.255" 
PORT = "8000"
URL = f"http://{RADMIN_IP}:{PORT}/test-connection"

print("========================================")
print(f" Interface Terminal -> Connecting to {RADMIN_IP}")
print("========================================")

while True:
    user_query = input("\nEnter your query (or type 'exit' to quit): ")
    
    if user_query.strip().lower() == 'exit':
        print("Closing interface...")
        break
        
    if not user_query.strip():
        continue

    print("Sending to Cloud PC...")
    try:
        # Send the POST request to the Cloud PC
        response = requests.post(URL, json={"query": user_query}, timeout=5)
        response.raise_for_status() # Check for HTTP errors
        
        # Parse and print the response
        data = response.json()
        print(f"[CLOUD RESPONSE]: {data['reply']}")
        
    except requests.exceptions.ConnectionError:
        print("\n[ERROR] Connection refused! Is the server running and is the Firewall open?")
    except requests.exceptions.Timeout:
        print("\n[ERROR] Connection timed out. The Radmin IP might be wrong or blocked.")
    except Exception as e:
        print(f"\n[ERROR] Something went wrong: {e}")