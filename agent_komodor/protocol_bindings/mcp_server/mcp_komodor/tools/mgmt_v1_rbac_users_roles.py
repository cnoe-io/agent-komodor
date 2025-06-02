
"""Tools for /mgmt/v1/rbac/users/roles operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def rbacuserrolescontrollerv1_post(body_userId: str, body_roleId: str, body_expiration: str) -> Dict[str, Any]:
    '''
    Creates a new role assignment for a user in the RBAC system.

    Args:
        body_userId (str): The ID of the user to whom the role is being assigned.
        body_roleId (str): The ID of the role to be assigned to the user.
        body_expiration (str): The expiration date for the role assignment.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing details of the role assignment.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      post:
        summary: Assign a role to a user
        operationId: rbacuserrolescontrollerv1_post
        requestBody:
          content:
            application/json:
              schema:
                type: object
                properties:
                  userId:
                    type: string
                    description: The ID of the user.
                  roleId:
                    type: string
                    description: The ID of the role.
                  expiration:
                    type: string
                    format: date-time
                    description: The expiration date for the role assignment.
        responses:
          '200':
            description: Successful role assignment
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    success:
                      type: boolean
                      description: Indicates if the role was successfully assigned.
                    data:
                      type: object
                      description: Details of the role assignment.
          '400':
            description: Bad request
          '500':
            description: Internal server error
    '''
    logger.debug("Making POST request to /mgmt/v1/rbac/users/roles")
    params = {}
    data = None
    

    

    

    


    
    data = {}

    
    data["userId"] = body_userId
    

    
    data["roleId"] = body_roleId
    

    
    data["expiration"] = body_expiration
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/users/roles",
        method="POST",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def rbacuserrolescontrollerv1_delete(body_userId: str, body_roleId: str, body_expiration: str) -> Dict[str, Any]:
    '''
    Deletes a user role in the RBAC system.

    Args:
        body_userId (str): The ID of the user whose role is to be deleted.
        body_roleId (str): The ID of the role to be deleted from the user.
        body_expiration (str): The expiration date for the role assignment.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      delete:
        summary: Delete a user role in the RBAC system.
        operationId: rbacuserrolescontrollerv1_delete
        parameters:
          - name: body_userId
            in: query
            description: The ID of the user whose role is to be deleted.
            required: true
            schema:
              type: string
          - name: body_roleId
            in: query
            description: The ID of the role to be deleted from the user.
            required: true
            schema:
              type: string
          - name: body_expiration
            in: query
            description: The expiration date for the role assignment.
            required: true
            schema:
              type: string
        responses:
          '200':
            description: Successful deletion of the user role.
            content:
              application/json:
                schema:
                  type: object
          '400':
            description: Bad request due to invalid input.
          '404':
            description: User or role not found.
          '500':
            description: Internal server error.
    '''
    logger.debug("Making DELETE request to /mgmt/v1/rbac/users/roles")
    params = {}
    data = None
    

    

    

    


    
    data = {}

    
    data["userId"] = body_userId
    

    
    data["roleId"] = body_roleId
    

    
    data["expiration"] = body_expiration
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/users/roles",
        method="DELETE",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
