from flask import Flask, request, render_template_string, redirect, url_for
import socket
import logging

# Initialize the Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def is_reachable(host, port):
    """Check if a host is reachable on a specific port and log details."""
    log = []  # Collect logs
    try:
        log.append(f"Attempting to connect to {host}:{port}...")
        sock = socket.create_connection((host, port), timeout=10)
        sock.close()
        log.append(f"Connection to {host}:{port} established successfully.")
        return True, '\n'.join(log)
    except socket.timeout:
        log.append(f"Connection to {host}:{port} timed out.")
        return False, '\n'.join(log)
    except socket.error as e:
        log.append(f"Socket error: {str(e)}")
        return False, '\n'.join(log)

@app.route('/', methods=['GET', 'POST'])
def check_reachability():
    """Endpoint to check reachability of a host and port."""
    if request.method == 'POST':
        # Retrieve form data
        host = request.form['host']
        port = int(request.form['port'])
        # Check reachability
        reachable, connection_log = is_reachable(host, port)
        status = 'reachable' if reachable else 'not reachable'

        # Redirect with results as query parameters
        return redirect(url_for('check_reachability', host=host, port=port, status=status, response=connection_log))

    # Retrieve query parameters in GET request
    status = request.args.get('status')
    host = request.args.get('host')
    port = request.args.get('port')
    response = request.args.get('response')

    # Render the template
    return render_template_string(TEMPLATE, status=status, host=host, port=port, response=response)

# HTML template for the web page
TEMPLATE = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Validate Connectivity to Remote Host</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f9;
        margin: 0;
        padding: 0;
      }
      .container {
        background: #ffffff;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        max-width: 600px;
        margin: 2rem auto 0;
      }
      h1 {
        font-size: 1.75rem;
        margin-bottom: 1rem;
        color: #333;
        text-align: center;
      }
      label {
        font-size: 0.9rem;
        color: #555;
      }
      input {
        width: 100%;
        padding: 0.8rem;
        margin: 0.5rem 0 1rem;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-size: 1rem;
      }
      button {
        width: 100%;
        padding: 0.8rem;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 4px;
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 0.3s ease;
      }
      button:hover {
        background-color: #0056b3;
      }
      .status {
        margin-top: 1rem;
        padding: 1rem;
        border-radius: 4px;
        font-size: 0.95rem;
        text-align: center;
      }
      .reachable {
        background-color: #d4edda;
        color: #155724;
      }
      .not-reachable {
        background-color: #f8d7da;
        color: #721c24;
      }
      .response {
        margin-top: 2rem;
        background: #f1f1f1;
        padding: 1rem;
        border-radius: 8px;
        font-size: 0.9rem;
        color: #333;
        word-wrap: break-word;
        white-space: pre-wrap;
      }
      .new-search {
        margin-top: 1.5rem;
        text-align: center;
      }
      .new-search button {
        padding: 0.8rem 1.5rem;
        background-color: #6c757d;
        color: white;
        border: none;
        border-radius: 4px;
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 0.3s ease;
      }
      .new-search button:hover {
        background-color: #5a6268;
      }
      footer {
        text-align: center;
        margin-top: 2rem;
        font-size: 0.9rem;
        color: #777;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Validate Connectivity to Remote Host</h1>
      <form method="post">
        <label for="host">Host:</label>
        <input type="text" id="host" name="host" placeholder="Enter host (e.g., example.com)" required>
        
        <label for="port">Port:</label>
        <input type="number" id="port" name="port" placeholder="Enter port (e.g., 22)" required>
        
        <button type="submit">Check</button>
      </form>
      
      {% if status %}
        <div class="status {{ 'reachable' if status == 'reachable' else 'not-reachable' }}">
          Connection to <strong>{{ host }}</strong>:<strong>{{ port }}</strong> is <strong>{{ status }}</strong>.
        </div>
      {% endif %}

      {% if response %}
        <div class="response">
          <strong>Server Response:</strong>
          <pre>{{ response }}</pre>
        </div>
      {% endif %}
      
      {% if status or response %}
        <div class="new-search">
          <form action="/" method="get">
            <button type="submit">New Search</button>
          </form>
        </div>
      {% endif %}
    </div>

    <footer>
      <div style="display: flex; align-items: center; justify-content: center; gap: 10px;">
        <img src="/static/solo-logo.png" alt="Solo Orbit Logo" style="width: 30px; height: auto;">
        <span>Powered by <strong>Solo Orbit</strong></span>
      </div>
    </footer>
  </body>
</html>
'''

if __name__ == '__main__':
    # Ensure the app listens on all interfaces and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)

