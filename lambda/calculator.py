import json

def lambda_handler(event, context):
    
    body = json.loads(event['body'])
    
    oneValue = body.get('oneValue')
    anotherValue = body.get('anotherValue')
    operation = body.get('operation')
    response = 0
    
    try:
        if oneValue is None:
            raise Exception('oneValue não pode ser vazio ou nulo')
    except Exception:
        return {
            'statusCode': 400,
            'body': 'oneValue não pode ser vazio ou nulo'
        }
        
    try:
        if anotherValue is None:
            raise Exception('anotherValue não pode ser vazio ou nulo')
    except Exception:
        return {
            'statusCode': 400,
            'body': 'anotherValue não pode ser vazio ou nulo'
        }
        
    try:
        if operation is None:
            raise Exception('operation não pode ser vazio ou nulo')
    except Exception:
        return {
            'statusCode': 400,
            'body': 'operation não pode ser vazio ou nulo'
        }
        
    try:    
        if not isinstance(oneValue, (int, float)):
            raise Exception('oneValue precisa ser numerico')
    except Exception:
        return {
            'statusCode': 400,
            'body': 'oneValue precisa ser numerico'
        }
        
    try:    
        if not isinstance(anotherValue, (int, float)):
            raise Exception('anotherValue precisa ser numerico')
    except Exception:
        return {
            'statusCode': 400,
            'body': 'anotherValue precisa ser numerico'
        }
        
    try:    
        if not isinstance(operation, (str)):
            raise Exception('operation precisa ser um texto')
    except Exception:
        return {
            'statusCode': 400,
            'body': 'operation precisa ser um texto'
        }
        
    try:
        if operation != 'plus' and operation != 'minus' and operation != 'times' and operation != 'divided':
            raise Exception('operation precisa ser: minus, plus, times ou divided')
    except Exception:
        return {
            'statusCode': 400,
            'body': 'operation precisa ser: minus, plus, times ou divided'
        }
        
    if operation == 'plus':
        response = oneValue + anotherValue
        
    if operation == 'minus':
        response = oneValue - anotherValue
        
    if operation == 'times':
        response = oneValue * anotherValue
    
    try:    
        if operation == 'divided':
            if anotherValue == 0:
                raise Exception('anotherValue não pode ser zero')
            response = oneValue / anotherValue
    except Exception:
        return {
            'statusCode': 400,
            'body': 'anotherValue não pode ser zero'
        }
        
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
