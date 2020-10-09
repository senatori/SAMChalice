import json
from chalice import Chalice

app = Chalice(app_name='chalice-sam-jenkins')

CITIES_TO_STATE = {
    'seattle': 'WA',
    'portland': 'OR',
}

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/cities/{city}')
def state_of_city(city):
    return {'state': CITIES_TO_STATE[city]}

@app.route('/hello/{name}')
def hello_name(name):
   # '/hello/james' -> {"hello": "james"}
   return {'hello': name}

@app.route('/users', methods=['POST'])
def create_user():
    # This is the JSON body the user sent in their POST request.
    user_as_json = app.current_request.json_body
    # We'll echo the json body back to the user in a 'user' key.
    return {'user': user_as_json}

#current_request.query_params - A dict of the query params.
# current_request.headers - A dict of the request headers.
# current_request.uri_params - A dict of the captured URI params.
# current_request.method - The HTTP method (as a string).
# current_request.json_body - The parsed JSON body.
# current_request.raw_body - The raw HTTP body as bytes.
# current_request.context - A dict of additional context information
# current_request.stage_vars - Configuration for the API Gateway stage
#



# def lambda_handler(event, context):
#     """Sample pure Lambda function
#
#     Parameters
#     ----------
#     event: dict, required
#         API Gateway Lambda Proxy Input Format
#
#         Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
#
#     context: object, required
#         Lambda Context runtime methods and attributes
#
#         Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html
#
#     Returns
#     ------
#     API Gateway Lambda Proxy Output Format: dict
#
#         Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
#     """
#
#     # try:
#     #     ip = requests.get("http://checkip.amazonaws.com/")
#     # except requests.RequestException as e:
#     #     # Send some context about this error to Lambda Logs
#     #     print(e)
#
#     #     raise e
#
#     return {
#         "statusCode": 200,
#         "body": json.dumps({
#             "message": "hello claurice",
#             # "location": ip.text.replace("\n", "")
#         }),
#     }
