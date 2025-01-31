## HNG Stage 0 Back-End

This project is about developing a Public API to retrieve basic information

## Description

Develop a Public API that returns the following information in JSON format:
1. Your registered email address (used to register on the HNG12 Slack workspace).
2. The current datetime as an ISO 8601 formatted timestamp.
3. The Github URL of the project's codebase.

## Requirements
1. Technology stack:
2. Programming language/framework: Use any of the following: C#, PHP, Python, Go, Java, JavaScript, Typescript.
3. Deployment: The API must be deployed to a publicly accessible endpoint.
4. CORS Handling: Ensure the API handles Cross-Origin Resource Sharing (CORS) appropriately.
5. Response Format: All responses must be in JSON format.

## API Specification 
. Endpoint: GET**
. Required JSON Response Format (200 OK):

"email": "your-email@example.com",
"current_datetime": "2025-01-30T09:30:00Z",
"github_url": "<https://github.com/yourusername/your-repo>"

## Acceptance Criteria 
. The API must accept GET requests and return the required JSON response 
. The current_datetime field must be dynamically generated in ISO 8601 format (UTC).
. Provides appropriate HTTP status code

## Usage

run the requirement.txt file using -r flag
then run ./startup.sh script to deploy locally 

## Technology and Stack

<https://hng.tech/hire/python-developers>
