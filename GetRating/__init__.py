import logging
import json
import azure.functions as func


def main(req: func.HttpRequest, ratings: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if not ratings:
        return func.HttpResponse(f"Hello, nothing found",status_code=404)
    else:
        return func.HttpResponse(
              ratings[0].to_json(),
             status_code=200


        )


