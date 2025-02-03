## HNG Stage 1 Backend

This project is about creating an API that takes a number and returns an interesting mathematical property about it, along with a fun fact.

## Requirements
1. Technology Stack:
   Use any programming language or framework of your choice (See Sharp (C #), PHP :elephant:, Python :snake:, Go :runner::skin-tone-5:, Java :coffee:, JS/TS :nauseated_face:)
   Must be deployed to a publicly accessible endpoint
   Must handle CORS (Cross-Origin Resource Sharing)
   Must return responses in JSON format
2. Version Control:
   Code must be hosted on GitHub
   Repository must be public
   Must include a well-structured

## API Specification
> Endpoint: GET** <your-domain.com>/api/classify-number?number=371
> Required JSON Response Format (200 OK):
  { "number": 371, "is_prime": false, "is_perfect": false, "properties": ["armstrong", "odd"], "digit_sum": 11 // sum of its digits, "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371" //gotten from the numbers API } 
> Required JSON Response Format (400 Bad Request):
  {"number": "alphabet", "error": true}

## Acceptance Criteria Functionality
. Accepts GET requests with a number parameter.
. Returns JSON in the specified format.
. Accepts all valid integers as the only possible inputs.
. Provides appropriate HTTP status code.

## Code Quality
. Organized code structure.
. Basic error handling and input validation.
. Avoids hardcoded values.

## Deployment
. Publicly accessible and stable API.
. Fast response time (< 500ms).
