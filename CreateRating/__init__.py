import logging

import azure.functions as func
import json
import uuid
from datetime import datetime, timezone
import requests
import os


def main(req: func.HttpRequest , doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    getProductbyIdURL = "https://serverlessohapi.azurewebsites.net/api/GetProduct"
    getUserbyIdURL = "https://serverlessohapi.azurewebsites.net/api/GetUser"
    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        userId = req_body.get('userId')
        productId = req_body.get('productId')
        rating = req_body.get('rating')
        resp_body = req_body
        
        resp_body["id"] = str(uuid.uuid4())
        resp_body["timestamp"] = str(datetime.now(timezone.utc))
    if rating > 5 or rating <0:
        return func.HttpResponse(
             "The rating should be between 0 and 5",
             status_code=400
        )
    if userId:
        checkUserIdRequest = requests.get(url = getUserbyIdURL, params = {'userId':userId})
        if checkUserIdRequest.status_code == 200:
             if productId:
                checkproductIdRequest = requests.get(url = getProductbyIdURL, params = {'productId':productId})
                if checkproductIdRequest.status_code == 200:
                    doc.set(func.Document.from_json(json.dumps(resp_body)))
                    return func.HttpResponse(json.dumps(resp_body), mimetype="application/json")
                else:
                    return func.HttpResponse(
                        "productId Not Found",
                        status_code=400
                    )
             else:
                return func.HttpResponse(
                "productId Not Specified",
                status_code=400
            )
            #return func.HttpResponse(json.dumps(resp_body), mimetype="application/json")
        else:
            return func.HttpResponse(
             "UserID Not Found",
             status_code=400
        )
    else:
        return func.HttpResponse(
             "UserID Not Specified",
             status_code=400
        )
