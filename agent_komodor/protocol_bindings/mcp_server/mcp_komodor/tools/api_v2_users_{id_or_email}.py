
"""Tools for /api/v2/users/{id_or_email} operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def get_api_v2_users_id_or_email(path_id_or_email: str) -> Dict[str, Any]:
    '''
    Get a User by id or email.

    Args:
        path_id_or_email (str): The user's ID or email address to retrieve.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing user details.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        paths:
          /api/v2/users/{id_or_email}:
            get:
              summary: Retrieve a user by ID or email.
              parameters:
                - name: id_or_email
                  in: path
                  required: true
                  description: The ID or email of the user to retrieve.
                  schema:
                    type: string
              responses:
                '200':
                  description: Successful response with user details.
                  content:
                    application/json:
                      schema:
                        type: object
                        properties:
                          id:
                            type: string
                          email:
                            type: string
                          name:
                            type: string
                '404':
                  description: User not found.
                '500':
                  description: Internal server error.
    '''
    logger.debug("Making GET request to /api/v2/users/{id_or_email}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/users/{id_or_email}",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def put_api_v2_users_id_or_email(path_id_or_email: str, body_displayName: str = None, body_roleIds: List[str] = None, body_roleNames: List[str] = None) -> Dict[str, Any]:
    '''
    Update a User by id or email.

    Args:
        path_id_or_email (str): The user's ID or email to identify the user to be updated.
        body_displayName (str, optional): The new display name for the user. Defaults to None.
        body_roleIds (List[str], optional): A list of role IDs to assign to the user. Defaults to None.
        body_roleNames (List[str], optional): A list of role names to assign to the user. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing the updated user information.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        put:
          summary: Update a User by id or email
          operationId: put_api_v2_users_id_or_email
          parameters:
            - name: path_id_or_email
              in: path
              required: true
              schema:
                type: string
              description: The user's ID or email.
          requestBody:
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    displayName:
                      type: string
                      description: The new display name for the user.
                    roleIds:
                      type: array
                      items:
                        type: string
                      description: A list of role IDs to assign to the user.
                    roleNames:
                      type: array
                      items:
                        type: string
                      description: A list of role names to assign to the user.
          responses:
            '200':
              description: Successful response with updated user information.
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties: true
            '400':
              description: Bad request due to invalid input.
            '404':
              description: User not found.
            '500':
              description: Internal server error.
    '''
    logger.debug("Making PUT request to /api/v2/users/{id_or_email}")
    params = {}
    data = None
    

    

    

    

    


    
    data = {}

    

    
    data["displayName"] = body_displayName
    

    
    data["roleIds"] = body_roleIds
    

    
    data["roleNames"] = body_roleNames
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/users/{id_or_email}",
        method="PUT",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def delete_api_v2_users_id_or_email(path_id_or_email: str) -> Dict[str, Any]:
    '''
    Delete a User by id or email.

    Args:
        path_id_or_email (str): The ID or email of the user to be deleted.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing the result of the deletion operation.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        delete:
          summary: Delete a User by id or email
          operationId: deleteApiV2UsersIdOrEmail
          parameters:
            - name: path_id_or_email
              in: path
              required: true
              description: The ID or email of the user to be deleted
              schema:
                type: string
          responses:
            '200':
              description: User successfully deleted
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties: true
            '400':
              description: Invalid ID or email supplied
            '404':
              description: User not found
            '500':
              description: Internal server error
    '''
    logger.debug("Making DELETE request to /api/v2/users/{id_or_email}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/users/{id_or_email}",
        method="DELETE",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
