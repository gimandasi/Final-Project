import json

def lambda_handler(event, context):
    method = event.get("httpMethod", "GET")

    if method == "GET":
        return {
            "statusCode": 200,
            "body": json.dumps([
                {"item": "Apples"},
                {"item": "Chicken"},
                {"item": "Rice"}
            ])
        }

    elif method == "DELETE":
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Item removed"})
        }

    return {
        "statusCode": 400,
        "body": json.dumps({"error": "Unsupported method"})
    }
