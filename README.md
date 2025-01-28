<H1>Host-Reach App by Solo Orbit</H1>

A Flask-based web application to validate the connectivity of remote hosts on specific ports. This tool allows users to check the reachability of a host and displays detailed logs of the connection process. The intent of the design is to provide a lightweight alternative to telnet clients and other tooling.

<h2>Features</h2>

User-friendly web interface to check host and port reachability.
Displays connection status (reachable or not reachable).
Logs detailed connection attempts for troubleshooting.
Includes a "New Search" button to reset and start fresh.
The application utilizes Flask and Python.

<h2>Setup Instructions</h2>

1. Clone the Repository
    - git clone https://github.com/dwhjr/host-reach.git
    - cd host-reach
2. Install Requirements
    - Create a virtual environment and install the required Python packages:
        - python -m venv venv
        - source venv/bin/activate   # For Linux/macOS
        - venv\Scripts\activate      # For Windows
        - pip install -r requirements.txt
3. Run the Application
    - Run the Flask app:
    - python app/static/app.py
    - By default, the application runs on http://localhost:5000.
4. Access the Web App
    - Visit the app in your browser at:
    - http://localhost:5001
5. Docker Support
    - To containerize the application:
        - 1. Build the Docker Image
            - docker build -t host-reach .
        - 2. Run the Docker Container
            - docker run -p 5001:5000 host-reach
    - The app will be available at http://localhost:5001.

## Project Structure
```
\Project-root-folder
├── Dockerfile              # Docker build instructions
├── app
│   ├── app.py              # Main Flask application
│   └── static
│       └── logo            # Project logo
├── docker-compose.yml      # Docker Compose configuration
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```
<h2>Screenshots</h2>

Search Interface

![image](https://github.com/user-attachments/assets/9a77b2c6-d94d-4fe1-b70b-fb92e617134d)

Result Screen

![image](https://github.com/user-attachments/assets/ec1722b3-bca2-4159-9950-31bd3f048ca3)

<h2>Contributing</h2>

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or fixes.

<h2>License</h2>

This project is licensed under the MIT License.

<h2>Acknowledgments and Parting Thoughts</h2>
- Powered by Solo Orbit</br>
- Built using Flask and Python</br>
- Be Kind</br>
- Pals</br>
- By God Woodrow, you just never get the point do you? It ain't dying I am talking about, it's living.
