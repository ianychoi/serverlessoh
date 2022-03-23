import logging
import json
import azure.functions as func


def main(req: func.HttpRequest, ratings: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

#    name = req.params.get('name')
    if not ratings:
        return func.HttpResponse(f"Hello, nothing found",status_code=200)
    else:
        returnList = []
        for rating in ratings:
            returnList.append(rating.to_json())

        return func.HttpResponse(                            
             json.dumps(returnList),
             status_code=200
        )


