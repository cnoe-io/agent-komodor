
"""Tools for /mgmt/v1/rbac/roles operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def rolescontrollerv1_getall() -> Dict[str, Any]:
    '''
    Fetches all roles from the RBAC management API.

    Args:
        None

    Returns:
        Dict[str, Any]: The JSON response from the API call containing all roles.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Retrieve all roles
          operationId: rolescontrollerv1_getall
          responses:
            '200':
              description: A list of roles
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties:
                      type: object
            '400':
              description: Bad Request
            '401':
              description: Unauthorized
            '500':
              description: Internal Server Error
    '''
    logger.debug("Making GET request to /mgmt/v1/rbac/roles")
    params = {}
    data = None
    


    
    data = {}

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/roles",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def rolescontrollerv1_post(body_name: str) -> Dict[str, Any]:
    '''
    Creates a new role in the RBAC system.

    Args:
        body_name (str): The name of the role to be created.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing details of the created role.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      post:
        summary: Create a new role
        operationId: rolescontrollerv1_post
        requestBody:
          required: true
          content:
            application/json:
              schema:
                type: object
                properties:
                  name:
                    type: string
                    description: The name of the role to be created.
        responses:
          '200':
            description: Role created successfully
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    id:
                      type: string
                      description: The unique identifier of the created role.
                    name:
                      type: string
                      description: The name of the created role.
          '400':
            description: Bad request
          '500':
            description: Internal server error
    '''
    logger.debug("Making POST request to /mgmt/v1/rbac/roles")
    params = {}
    data = None
    

    


    
    data = {}

    
    data["name"] = body_name
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/roles",
        method="POST",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def rolescontrollerv1_delete(body_id: str) -> Dict[str, Any]:
    '''
    Deletes a role by its ID.

    Args:
        body_id (str): The ID of the role to be deleted.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing the result of the delete operation.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      delete:
        summary: Delete a role by ID
        operationId: rolescontrollerv1_delete
        parameters:
          - name: body_id
            in: path
            required: true
            description: The ID of the role to be deleted
            schema:
              type: string
        responses:
          '200':
            description: Role successfully deleted
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    success:
                      type: boolean
                      description: Indicates if the deletion was successful
          '400':
            description: Invalid ID supplied
          '404':
            description: Role not found
          '500':
            description: Internal server error
    '''
    logger.debug("Making DELETE request to /mgmt/v1/rbac/roles")
    params = {}
    data = None
    

    


    
    data = {}

    
    data["id"] = body_id
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/roles",
        method="DELETE",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
