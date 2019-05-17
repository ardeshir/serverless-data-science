try:
  import unzip_requirements
except ImportError:
  pass

import json

def trainHandler(event, context):
    body = json.loads( event.get('body') )

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
