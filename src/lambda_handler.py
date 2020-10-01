import lambda_wsgi
from sample.wsgi import application as app


def lambda_handler(event, context):
    return lambda_wsgi.response(app, event, context)
