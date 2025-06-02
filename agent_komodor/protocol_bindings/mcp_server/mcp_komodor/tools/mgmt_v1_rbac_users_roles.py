
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
        body_expiration (str): The expiration date of the role assignment.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing details of the role assignment.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        paths:
          /mgmt/v1/rbac/users/roles:
            post:
              summary: Assign a role to a user
              requestBody:
                required: true
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
                          description: The expiration date of the role assignment.
              responses:
                '200':
                  description: Role assignment successful
                  content:
                    application/json:
                      schema:
                        type: object
                        properties:
                          userId:
                            type: string
                          roleId:
                            type: string
                          expiration:
                            type: string
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
        Dict[str, Any]: The JSON response from the API call indicating success or failure.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        delete:
          summary: Deletes a user role in the RBAC system.
          operationId: rbacuserrolescontrollerv1_delete
          parameters:
            - name: body_userId
              in: body
              required: true
              schema:
                type: string
              description: The ID of the user whose role is to be deleted.
            - name: body_roleId
              in: body
              required: true
              schema:
                type: string
              description: The ID of the role to be deleted from the user.
            - name: body_expiration
              in: body
              required: true
              schema:
                type: string
              description: The expiration date for the role assignment.
          responses:
            '200':
              description: Role successfully deleted.
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties: true
            '400':
              description: Bad request due to invalid parameters.
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
