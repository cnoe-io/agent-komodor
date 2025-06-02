
"""Tools for /mgmt/v1/rbac/actions operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def actionscontrollerv1_getall() -> Dict[str, Any]:
    '''
    Fetches all actions from the RBAC management API.

    Args:
        None

    Returns:
        Dict[str, Any]: The JSON response from the API call containing all actions.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Retrieve all actions
          operationId: actionscontrollerv1_getall
          responses:
            '200':
              description: A list of actions
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties:
                      type: string
            '400':
              description: Bad Request
            '401':
              description: Unauthorized
            '500':
              description: Internal Server Error
    '''
    logger.debug("Making GET request to /mgmt/v1/rbac/actions")
    params = {}
    data = None
    


    
    data = {}

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/actions",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def actionscontrollerv1_post(body_action: str, body_description: str, body_k8sRuleset: List[str]) -> Dict[str, Any]:
    '''
    Makes an asynchronous POST request to the /mgmt/v1/rbac/actions endpoint.

    Args:
        body_action (str): The action to be performed, corresponding to the OpenAPI parameter 'body_action'.
        body_description (str): A description of the action, corresponding to the OpenAPI parameter 'body_description'.
        body_k8sRuleset (List[str]): A list of Kubernetes rulesets, corresponding to the OpenAPI parameter 'body_k8sRuleset'.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        paths:
          /mgmt/v1/rbac/actions:
            post:
              summary: Create a new RBAC action
              requestBody:
                required: true
                content:
                  application/json:
                    schema:
                      type: object
                      properties:
                        action:
                          type: string
                          description: The action to be performed.
                        description:
                          type: string
                          description: A description of the action.
                        k8sRuleset:
                          type: array
                          items:
                            type: string
                          description: A list of Kubernetes rulesets.
              responses:
                '200':
                  description: Successful response
                  content:
                    application/json:
                      schema:
                        type: object
                        additionalProperties: true
                '400':
                  description: Bad Request
                '500':
                  description: Internal Server Error
    '''
    logger.debug("Making POST request to /mgmt/v1/rbac/actions")
    params = {}
    data = None
    

    

    

    


    
    data = {}

    
    data["action"] = body_action
    

    
    data["description"] = body_description
    

    
    data["k8sRuleset"] = body_k8sRuleset
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/actions",
        method="POST",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
