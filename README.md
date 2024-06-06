# Fake Payment Server
A simple Flask server that simulates a payment endpoint with customizable responses, can be used to test payment methods in web applications or for penetration testing.

usage :  `python3 fake_payment_endpoint.py [-h] [-p PORT] [-a ADDITIONAL] [-m MESSAGE] [-c CODE] [-d DATA]`

Fake Payment Server

    optional arguments:
      -h, --help            show this help message and exit
      -p PORT, --port PORT  Port to run the server on
      -a ADDITIONAL, --additional ADDITIONAL
                            Additional values to read from request
      -m MESSAGE, --message MESSAGE
                            Fake message to be returned
      -c CODE, --code CODE  Fake code to be returned
      -d DATA, --data DATA  JSON string containing enforced values 
      
example :  `python3 fake_payment_endpoint.py -p 8080 -c 201 -m "New Payment Success" -a country,method -d '{"currency": "EUR", "method": "cash"}'`

testing : `curl -X POST -H "Content-Type: application/json" -d '{"amount":100.0,"country":"France","currency":"EUR","method":"cash","transaction_id":"1234567890"}' http://localhost:8080`

response : 
`{
    "amount": 100.0,
    "country": "France",
    "currency": "EUR",
    "message": "New Payment Success",
    "method": "cash",
    "status": "201",
    "transaction_id": "1234567890"
}`
