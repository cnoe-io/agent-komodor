
"""Tools for /mgmt/v1/rbac/policies/{id} operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def policiescontrollerv1_get(path_id: str) -> Dict[str, Any]:
    '''
    Fetches policy details using the specified path ID.

    Args:
        path_id (str): The identifier for the policy to retrieve.

    Returns:
        Dict[str, Any]: The JSON response containing policy details.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      get:
        summary: Retrieve policy details by ID
        operationId: policiescontrollerv1_get
        parameters:
          - name: path_id
            in: path
            required: true
            description: The identifier for the policy
            schema:
              type: string
        responses:
          200:
            description: Successful response with policy details
            content:
              application/json:
                schema:
                  type: object
                  additionalProperties: true
          404:
            description: Policy not found
          500:
            description: Server error
    '''
    logger.debug("Making GET request to /mgmt/v1/rbac/policies/{id}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        f"/mgmt/v1/rbac/policies/{path_id}",
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
    Updates a policy in the RBAC system with the specified name and statements.

    Args:
        path_id (str): The unique identifier of the policy to update.
        body_name (str): The new name for the policy.
        body_statements (List[str]): The list of statements defining the policy rules.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing the updated policy details.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        paths:
          /mgmt/v1/rbac/policies/{id}:
            put:
              summary: Update a policy
              parameters:
                - name: id
                  in: path
                  required: true
                  description: The unique identifier of the policy to update.
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
                          description: The new name for the policy.
                        statements:
                          type: array
                          items:
                            type: string
                          description: The list of statements defining the policy rules.
              responses:
                '200':
                  description: Successfully updated the policy.
                  content:
                    application/json:
                      schema:
                        type: object
                        properties:
                          name:
                            type: string
                          description: The updated name of the policy.
                          statements:
                            type: array
                            items:
                              type: string
                            description: The updated list of policy statements.
                '400':
                  description: Bad request due to invalid input.
                '404':
                  description: Policy not found.
                '500':
                  description: Internal server error.
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
        f"/mgmt/v1/rbac/policies/{path_id}",
        method="PUT",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
