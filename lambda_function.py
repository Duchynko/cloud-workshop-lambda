import json
import os

import requests


def lambda_handler(event, context):
    api_key = os.environ.get('API_KEY')
    coin_name = event['coin']
    url = f'https://rest.coinapi.io/v1/exchangerate/{coin_name}/EUR'

    try:
        response = requests.get(
            url=url,
            headers={
                'X-CoinAPI-Key': api_key,
                'Content-Type': 'application/json'
            }
        )
    except Exception:
        return {
            'statusCode': 500,
            'body': 'An unexpected error has occurred'
        }
    else:
        if response.status_code == 200:
            response_body = json.loads(response.text)
            rate = round(response_body.get('rate'), 2)
            return {
                'statusCode': 200,
                'body': f'{rate} {coin_name}-EUR'
            }
        else:
            return {
                'statusCode': response.status_code,
                'body': response.text
            }
