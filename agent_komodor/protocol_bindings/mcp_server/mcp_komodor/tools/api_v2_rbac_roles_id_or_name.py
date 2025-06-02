
"""Tools for /api/v2/rbac/roles/{id_or_name} operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def get_api_v2_rbac_roles_id_or_name(path_id_or_name: str) -> Dict[str, Any]:
    '''
    Get Role by ID or Name.

    Args:
        path_id_or_name (str): The ID or name of the role to retrieve.

    Returns:
        Dict[str, Any]: The JSON response containing the role details.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Get Role by ID or Name
          operationId: getRoleByIdOrName
          parameters:
            - name: path_id_or_name
              in: path
              required: true
              description: The ID or name of the role to retrieve.
              schema:
                type: string
          responses:
            '200':
              description: Successful response containing role details.
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties: true
            '404':
              description: Role not found.
            '500':
              description: Internal server error.
    '''
    logger.debug("Making GET request to /api/v2/rbac/roles/{id_or_name}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        f"/api/v2/rbac/roles/{path_id_or_name}",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def put_api_v2_rbac_roles_id_or_name(path_id_or_name: str, body_name: str = None, body_isDefault: bool = None, body_policyIds: List[str] = None, body_policyNames: List[str] = None) -> Dict[str, Any]:
    '''
    Update Role by ID or Name.

    Args:
        path_id_or_name (str): The ID or name of the role to update.
        body_name (str, optional): The new name for the role. Defaults to None.
        body_isDefault (bool, optional): Indicates if the role is default. Defaults to None.
        body_policyIds (List[str], optional): List of policy IDs associated with the role. Defaults to None.
        body_policyNames (List[str], optional): List of policy names associated with the role. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        put:
          summary: Update Role by ID or Name
          operationId: put_api_v2_rbac_roles_id_or_name
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
                    isDefault:
                      type: boolean
                    policyIds:
                      type: array
                      items:
                        type: string
                    policyNames:
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
    '''
    logger.debug("Making PUT request to /api/v2/rbac/roles/{id_or_name}")
    params = {}
    data = None
    

    

    

    

    

    


    
    data = {}

    

    
    data["name"] = body_name
    

    
    data["isDefault"] = body_isDefault
    

    
    data["policyIds"] = body_policyIds
    

    
    data["policyNames"] = body_policyNames
    

    if not data:
        data = None
    success, response = await make_api_request(
        f"/api/v2/rbac/roles/{path_id_or_name}",
        method="PUT",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def delete_api_v2_rbac_roles_id_or_name(path_id_or_name: str) -> Dict[str, Any]:
    '''
    Delete Role by ID or Name.

    Args:
        path_id_or_name (str): The ID or name of the role to be deleted.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing the result of the delete operation.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        delete:
          summary: Delete Role by ID or Name
          operationId: deleteApiV2RbacRolesIdOrName
          parameters:
            - name: path_id_or_name
              in: path
              required: true
              description: The ID or name of the role to be deleted.
              schema:
                type: string
          responses:
            '200':
              description: Role successfully deleted.
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties: true
            '404':
              description: Role not found.
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      error:
                        type: string
            '500':
              description: Server error.
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      error:
                        type: string
    '''
    logger.debug("Making DELETE request to /api/v2/rbac/roles/{id_or_name}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        f"/api/v2/rbac/roles/{path_id_or_name}",
        method="DELETE",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
