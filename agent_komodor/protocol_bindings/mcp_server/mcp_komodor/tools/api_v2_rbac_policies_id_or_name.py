
"""Tools for /api/v2/rbac/policies/{id_or_name} operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def get_api_v2_rbac_policies_id_or_name(path_id_or_name: str) -> Dict[str, Any]:
    '''
    Get Policy by ID or Name.

    Args:
        path_id_or_name (str): The ID or name of the policy to retrieve.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing policy details.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Get Policy by ID or Name
          operationId: getApiV2RbacPoliciesIdOrName
          parameters:
            - name: path_id_or_name
              in: path
              required: true
              description: The ID or name of the policy to retrieve.
              schema:
                type: string
          responses:
            '200':
              description: Successful response with policy details.
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties: true
            '404':
              description: Policy not found.
            '500':
              description: Server error.
    '''
    logger.debug("Making GET request to /api/v2/rbac/policies/{id_or_name}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        f"/api/v2/rbac/policies/{path_id_or_name}",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def put_api_v2_rbac_policies_id_or_name(path_id_or_name: str, body_name: str = None, body_statements: List[str] = None) -> Dict[str, Any]:
    '''
    Update Policy by Id or Name.

    Args:
        path_id_or_name (str): The ID or name of the policy to update.
        body_name (str, optional): The new name for the policy. Defaults to None.
        body_statements (List[str], optional): The statements to update in the policy. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        put:
          summary: Update Policy by Id or Name
          operationId: putApiV2RbacPoliciesIdOrName
          parameters:
            - name: path_id_or_name
              in: path
              required: true
              schema:
                type: string
          requestBody:
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    name:
                      type: string
                    statements:
                      type: array
                      items:
                        type: string
          responses:
            '200':
              description: Successful response
              content:
                application/json:
                  schema:
                    type: object
            '400':
              description: Bad Request
            '404':
              description: Policy not found
            '500':
              description: Internal Server Error
    '''
    logger.debug("Making PUT request to /api/v2/rbac/policies/{id_or_name}")
    params = {}
    data = None
    

    

    

    


    
    data = {}

    

    
    data["name"] = body_name
    

    
    data["statements"] = body_statements
    

    if not data:
        data = None
    success, response = await make_api_request(
        f"/api/v2/rbac/policies/{path_id_or_name}",
        method="PUT",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def delete_api_v2_rbac_policies_id_or_name(path_id_or_name: str) -> Dict[str, Any]:
    '''
    Delete a policy by its ID or name.

    Args:
        path_id_or_name (str): The ID or name of the policy to be deleted.

    Returns:
        Dict[str, Any]: The JSON response from the API call, which includes the status of the deletion.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      delete:
        summary: Delete a policy by ID or name.
        parameters:
          - name: path_id_or_name
            in: path
            required: true
            description: The ID or name of the policy to delete.
            schema:
              type: string
        responses:
          '200':
            description: Policy successfully deleted.
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    message:
                      type: string
                      example: "Policy deleted successfully."
          '404':
            description: Policy not found.
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    error:
                      type: string
                      example: "Policy not found."
          '500':
            description: Server error.
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    error:
                      type: string
                      example: "Internal server error."
    '''
    logger.debug("Making DELETE request to /api/v2/rbac/policies/{id_or_name}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        f"/api/v2/rbac/policies/{path_id_or_name}",
        method="DELETE",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
