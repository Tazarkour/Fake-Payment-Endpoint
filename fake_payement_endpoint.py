from flask import Flask, request, jsonify, make_response
import argparse
import json

app = Flask(__name__)

@app.route('/api/payments', methods=['POST','GET','DELETE', 'PUT'])
def fake_payment():
    
    
    default = {
        "amount": 100.00,
        "transaction_id": "1234567890",
        "currency": "USD",
        "status": "200",
        "message": "Payment processed successfully"
    }
    data = request.json
    print(f"Received payment request: {data}")
    if args.data:
        enforced_data = json.loads(args.data)
        default.update(enforced_data)
    else:
        enforced_data = {}
    if 'amount' in enforced_data:
        amount = enforced_data['amount']
    else:
        amount = data.get('amount', default["amount"]) 
    if 'transaction_id' in enforced_data:
        transaction_id = enforced_data['transaction_id']
    else:
        transaction_id = data.get('transaction_id', default["transaction_id"])
    if 'currency' in enforced_data:
        currency = enforced_data['currency']
    else:
        currency = data.get('currency', default["currency"])
    status = default["status"]
    message = default["message"]
    if args.code:
        status = args.code
    if args.message:
        message = args.message
    

    
    response = {
        'status': status,
        'message': message,
        'transaction_id': transaction_id,
        'amount': amount,
        'currency': currency
    }
    
    additional = args.additional.split(',') if args.additional else []
    for x in additional:
        if x in enforced_data:
            response[x] = enforced_data[x]
        else: 
            response[x] = data.get(x, default.get(x, None))
    
    response_body = jsonify(response)
    response_status = int(status)
    return make_response(response_body, response_status)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fake Payment Server')
    parser.add_argument('-p', '--port', type=int, default=5000, help='Port to run the server on')
    parser.add_argument("-a", "--additional", help="Additional values to read from request", required=False)
    parser.add_argument("-m", "--message", help="Fake message to be returned", required=False)
    parser.add_argument("-c", "--code", help="Fake code to be returned", required=False)
    parser.add_argument('-d', '--data', help='JSON string containing default values')
    args = parser.parse_args()
    if args.data:
        try:
            data = json.loads(args.data)
            
        except json.JSONDecodeError:
            print("Error: Invalid JSON data string provided.")
            exit(1)
    
    
    app.run(host='0.0.0.0', port=args.port)
