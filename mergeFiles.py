import http.server
import socketserver
import threading
import time
import requests
import json

# URLs of the JSON files (latest has highest priority for deduplication, so it will be kept)
urls = [
    "https://raw.githubusercontent.com/xneo1/portainer_templates/master/Template/template.json",
    "https://raw.githubusercontent.com/portainer/templates/master/templates-2.0.json"
]
def update_json():
    while True:
        combined = {"version": "2", "templates": []}
        added_templates = {}

        # Fetch each JSON file and combine them
        for url in urls:
            response = requests.get(url)
            data = response.json()
            for template in data.get("templates", []):
                identifier = f"{template.get('name', '')}-{template.get('image', '')}"
                combined["templates"].append(template)
                added_templates[identifier] = template

        # Replace combined templates with the latest version of each
        combined["templates"] = list(added_templates.values())

        # Write the combined list to a file
        with open('combined.json', 'w') as f:
            json.dump(combined, f)

        # Wait for 24 hours (86400 seconds)
        time.sleep(86400)

def serve_file(port):
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), Handler)
    print(f"Serving at port {port}")
    httpd.serve_forever()

# Create and start the update thread
update_thread = threading.Thread(target=update_json)
update_thread.start()

# Create and start the server thread
server_thread = threading.Thread(target=serve_file, args=[8008]) # adjust port number as needed
server_thread.start()
