import json

def lambda_handler(event, context):
    # Extracting numbers from the event
    number1 = event.get('number1')
    number2 = event.get('number2')
    
    # Checking if both numbers are provided
    if number1 is None or number2 is None:
        return {
            'statusCode': 400,
            'body': json.dumps('Both numbers must be provided.')
        }
    
    # Adding the two numbers
    result = number1 + number2
    
    # Returning the result
    return {
        'statusCode': 200,
        'body': json.dumps({
            'result': result
        })
    }
