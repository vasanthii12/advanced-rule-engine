# Advanced Rule Engine

This project implements an advanced rule engine with a web-based user interface for creating, combining, and evaluating complex rules.

## Table of Contents
1. [Features](#features)
2. [Design Choices](#design-choices)
3. [Dependencies](#dependencies)
4. [Setup Instructions](#setup-instructions)
5. [Running the Application](#running-the-application)
6. [API Documentation](#api-documentation)
7. [Contributing](#contributing)
8. [License](#license)

## Features
- Create complex rules with nested conditions
- Combine multiple rules
- Evaluate rules against user-provided data
- Visual representation of rule ASTs (Abstract Syntax Trees)

## Design Choices
- **Backend**: Python with Flask for its simplicity and flexibility in creating RESTful APIs.
- **Frontend**: HTML, CSS, and JavaScript for a lightweight, browser-based UI.
- **Rule Representation**: Rules are represented as ASTs for efficient processing and evaluation.
- **API Design**: RESTful API design for easy integration and scalability.

## Dependencies
- Python 3.8+
- Flask
- Flask-CORS
- Docker (optional, for containerized deployment)

## Setup Instructions

### Local Setup
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/advanced-rule-engine.git
   cd advanced-rule-engine
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Docker Setup
1. Ensure Docker is installed on your system.
2. Build the Docker image:
   ```
   docker build -t advanced-rule-engine .
   ```

## Running the Application

### Local Run
1. Start the Flask server:
   ```
   python app.py
   ```
2. Open a web browser and navigate to `http://localhost:5000`

### Docker Run
1. Run the Docker container:
   ```
   docker run -p 5000:5000 advanced-rule-engine
   ```
2. Open a web browser and navigate to `http://localhost:5000`

## API Documentation
- `POST /create_rule`: Create a new rule
  - Request body: `{ "rule": "rule string" }`
  - Response: `{ "message": "Rule created successfully", "ast": {...} }`

- `POST /combine_rules`: Combine multiple rules
  - Request body: `{ "rules": ["rule1", "rule2", ...] }`
  - Response: `{ "message": "Rules combined successfully", "ast": {...} }`

- `POST /evaluate_rule`: Evaluate a rule against provided data
  - Request body: `{ "ast": {...}, "data": {...} }`
  - Response: `{ "result": true/false }`

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
