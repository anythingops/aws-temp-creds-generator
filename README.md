# The Optimizer - AWS Temporary Credentials Generator

A secure web application for generating temporary AWS credentials through role assumption.

![The Optimizer](https://img.shields.io/badge/The%20Optimizer-AWS%20Credentials-orange)
![Flask](https://img.shields.io/badge/Flask-2.3.2-blue)
![Docker](https://img.shields.io/badge/Docker-Ready-brightgreen)

## Overview

The Optimizer is a lightweight web application that allows users to generate temporary AWS credentials by assuming IAM roles. This is particularly useful for:

- Developers who need to switch between different AWS roles
- Security teams implementing temporary access controls
- DevOps engineers managing multiple AWS environments
- Organizations implementing the principle of least privilege

## Features

- **Secure Credential Generation**: Generate temporary AWS credentials through role assumption
- **Modern UI**: Clean, responsive interface with intuitive form controls
- **Docker Support**: Easy deployment with Docker and docker-compose
- **Error Handling**: Robust error handling for API requests
- **Loading Indicators**: Visual feedback during credential generation

## Prerequisites

- Python 3.7+
- Docker and Docker Compose (for containerized deployment)
- AWS IAM user with permissions to assume roles
- AWS IAM roles configured with appropriate trust relationships

## Installation

### Local Development

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd my-app
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Access the application at http://localhost:5000

### Docker Deployment

1. Build and start the Docker container:
   ```bash
   docker-compose up --build
   ```

2. Access the application at http://localhost:3000

## Usage

1. Open the application in your web browser
2. Enter your AWS Access Key ID and Secret Access Key
3. Provide the ARN of the IAM role you want to assume
4. Click "Generate Credentials"
5. Copy the temporary credentials for use with AWS CLI or SDK

## Security Considerations

- This application handles sensitive AWS credentials. Deploy in a secure environment.
- Consider implementing additional security measures like HTTPS and authentication.
- Credentials are processed client-side and not stored on the server.
- Always follow AWS security best practices when handling access keys.

## Project Structure

```
my-app/
├── app.py                 # Flask application
├── docker-compose.yaml    # Docker Compose configuration
├── dockerfile             # Docker build instructions
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Frontend HTML template
└── README.md              # This file
```

## API Endpoints

- `GET /`: Serves the main application interface
- `POST /generate_temp_creds`: Generates temporary AWS credentials
  - Request body: `{ "access_key": "...", "secret_key": "...", "role_arn": "..." }`
  - Response: `{ "AccessKeyId": "...", "SecretAccessKey": "...", "SessionToken": "...", "Expiration": "..." }`

## Development

To modify the application:

1. Update the Flask routes in `app.py`
2. Modify the frontend in `templates/index.html`
3. Add any new dependencies to `requirements.txt`

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

- Built with [Flask](https://flask.palletsprojects.com/)
- AWS SDK for Python ([boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html))
- Icons by [Font Awesome](https://fontawesome.com/)
