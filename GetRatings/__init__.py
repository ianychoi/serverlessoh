import logging
import json
import azure.functions as func
import ast

def main(req: func.HttpRequest, ratings: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

#    name = req.params.get('name')
    if not ratings:
        return func.HttpResponse(f"Hello, nothing found",status_code=404)
    else:
        
        returnList = []
        for rating in ratings:
             ratingJson = rating.to_json()
             convertTrickyJson = ast.literal_eval(ratingJson)
             returnList.append(convertTrickyJson)

        return func.HttpResponse(                            
             str(returnList),
             status_code=200,
             mimetype="application/json"
        )


