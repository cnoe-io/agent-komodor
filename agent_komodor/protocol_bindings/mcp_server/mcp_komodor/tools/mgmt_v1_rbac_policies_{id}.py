
"""Tools for /mgmt/v1/rbac/policies/{id} operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def policiescontrollerv1_get(path_id: str) -> Dict[str, Any]:
    '''
    Fetches policy details from the RBAC management API using the specified path ID.

    Args:
        path_id (str): The identifier for the policy to be retrieved.

    Returns:
        Dict[str, Any]: The JSON response containing policy details from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Retrieve policy details
          operationId: policiescontrollerv1_get
          parameters:
            - name: path_id
              in: path
              required: true
              description: The identifier for the policy
              schema:
                type: string
          responses:
            '200':
              description: Successful response with policy details
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties: true
            '404':
              description: Policy not found
            '500':
              description: Internal server error
    '''
    logger.debug("Making GET request to /mgmt/v1/rbac/policies/{id}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/policies/{path_id}",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def policiescontrollerv1_updatepolicy(path_id: str, body_name: str, body_statements: List[str]) -> Dict[str, Any]:
    '''
    Updates a policy with the specified ID, name, and statements.

    Args:
        path_id (str): The ID of the policy to update.
        body_name (str): The new name for the policy.
        body_statements (List[str]): A list of statements to associate with the policy.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        put:
          summary: Update a policy
          operationId: updatePolicy
          parameters:
            - name: path_id
              in: path
              required: true
              description: The ID of the policy to update
              schema:
                type: string
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    name:
                      type: string
                      description: The new name for the policy
                    statements:
                      type: array
                      items:
                        type: string
                      description: A list of statements to associate with the policy
          responses:
            '200':
              description: Policy updated successfully
              content:
                application/json:
                  schema:
                    type: object
            '400':
              description: Bad request
            '404':
              description: Policy not found
            '500':
              description: Internal server error
    '''
    logger.debug("Making PUT request to /mgmt/v1/rbac/policies/{id}")
    params = {}
    data = None
    

    

    

    


    
    data = {}

    

    
    data["name"] = body_name
    

    
    data["statements"] = body_statements
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/policies/{path_id}",
        method="PUT",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
