# Pi-Velocity

Pi-Velocity is a high-speed transaction processing system for Pi Network, designed to ensure fast and efficient transactions.

## Getting Started

To get started with Pi-Velocity, follow these steps:

1. Clone the repository: `git clone https://github.com/KOSASIH/pi-velocity.git`
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install the dependencies: `pip install -r requirements.txt`
5. Run the application: `python3 app.py`

## API Documentation

Pi-Velocity uses FastAPI for its API documentation. To access the documentation, navigate to `http://localhost:8000/docs` in your web browser.

### API Endpoints

Pi-Velocity provides the following API endpoints:

- `/`: The root endpoint, which returns a simple message.
- `/transactions`: The transactions endpoint, which allows you to create and retrieve transactions.

### Transaction Endpoint

The transactions endpoint allows you to create and retrieve transactions.

#### Create a Transaction

To create a transaction, send a `POST` request to `/transactions` with the following JSON payload:

```json
{
  "sender": "address1",
  "receiver": "address2",
  "amount": 100
}
