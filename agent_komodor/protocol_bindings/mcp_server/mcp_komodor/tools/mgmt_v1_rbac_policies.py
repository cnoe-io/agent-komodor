
"""Tools for /mgmt/v1/rbac/policies operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def policiescontrollerv1_getall() -> Dict[str, Any]:
    '''
    Fetches all RBAC policies from the management API.

    Args:
        None

    Returns:
        Dict[str, Any]: The JSON response from the API call containing all RBAC policies.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Retrieve all RBAC policies
          operationId: policiescontrollerv1_getall
          responses:
            '200':
              description: A list of RBAC policies
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties:
                      type: object
            '400':
              description: Bad request
            '401':
              description: Unauthorized
            '500':
              description: Internal server error
    '''
    logger.debug("Making GET request to /mgmt/v1/rbac/policies")
    params = {}
    data = None
    


    
    data = {}

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/policies",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def policiescontrollerv1_post(body_name: str, body_statements: List[str]) -> Dict[str, Any]:
    '''
    Creates a new RBAC policy by making a POST request to the /mgmt/v1/rbac/policies endpoint.

    Args:
        body_name (str): The name of the policy to be created.
        body_statements (List[str]): A list of statements defining the policy rules.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing details of the created policy or an error message.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      post:
        summary: Create a new RBAC policy
        operationId: policiescontrollerv1_post
        requestBody:
          required: true
          content:
            application/json:
              schema:
                type: object
                properties:
                  name:
                    type: string
                    description: The name of the policy.
                  statements:
                    type: array
                    items:
                      type: string
                    description: The list of policy statements.
        responses:
          '200':
            description: Successful response
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    id:
                      type: string
                      description: The ID of the created policy.
                    name:
                      type: string
                      description: The name of the created policy.
                    statements:
                      type: array
                      items:
                        type: string
                      description: The statements of the created policy.
          '400':
            description: Bad Request
          '500':
            description: Internal Server Error
    '''
    logger.debug("Making POST request to /mgmt/v1/rbac/policies")
    params = {}
    data = None
    

    

    


    
    data = {}

    
    data["name"] = body_name
    

    
    data["statements"] = body_statements
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/policies",
        method="POST",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def policiescontrollerv1_delete(body_id: str) -> Dict[str, Any]:
    '''
    Deletes a policy identified by the given body_id.

    Args:
        body_id (str): The identifier of the policy to be deleted.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing the result of the delete operation.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        delete:
          summary: Delete a policy
          description: Deletes a policy identified by the given body_id.
          operationId: policiescontrollerv1_delete
          parameters:
            - name: body_id
              in: path
              required: true
              description: The identifier of the policy to be deleted.
              schema:
                type: string
          responses:
            '200':
              description: Successfully deleted the policy.
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      success:
                        type: boolean
                      message:
                        type: string
            '400':
              description: Invalid body_id supplied.
            '404':
              description: Policy not found.
            '500':
              description: Internal server error.
    '''
    logger.debug("Making DELETE request to /mgmt/v1/rbac/policies")
    params = {}
    data = None
    

    


    
    data = {}

    
    data["id"] = body_id
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/policies",
        method="DELETE",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
