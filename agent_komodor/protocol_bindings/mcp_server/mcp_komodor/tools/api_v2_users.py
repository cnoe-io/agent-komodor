
"""Tools for /api/v2/users operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def get_api_v2_users(param_displayName: str = None, param_email: str = None, param_isDeleted: bool = None) -> Dict[str, Any]:
    '''
    Get Users.

    Args:
        param_displayName (str, optional): The display name of the user to filter the results. Defaults to None.
        param_email (str, optional): The email of the user to filter the results. Defaults to None.
        param_isDeleted (bool, optional): Flag to filter users based on their deletion status. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing user information.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Retrieve a list of users.
          description: Fetch users based on optional filters such as display name, email, and deletion status.
          parameters:
            - name: param_displayName
              in: query
              description: The display name of the user.
              required: false
              schema:
                type: string
            - name: param_email
              in: query
              description: The email of the user.
              required: false
              schema:
                type: string
            - name: param_isDeleted
              in: query
              description: Filter users based on deletion status.
              required: false
              schema:
                type: boolean
          responses:
            '200':
              description: A list of users.
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties:
                      type: object
            '400':
              description: Bad request due to invalid parameters.
            '500':
              description: Internal server error.
    '''
    logger.debug("Making GET request to /api/v2/users")
    params = {}
    data = None
    

    
    params["displayName"] = param_displayName
    

    
    params["email"] = param_email
    

    
    params["isDeleted"] = param_isDeleted
    


    
    data = {}

    

    

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/users",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def post_api_v2_users(body_displayName: str, body_email: str, body_restoreIfDeleted: bool = None) -> Dict[str, Any]:
    '''
    Create a User.

    Args:
        body_displayName (str): The display name of the user to be created.
        body_email (str): The email address of the user to be created.
        body_restoreIfDeleted (bool, optional): Flag indicating whether to restore the user if they were previously deleted. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        post:
          summary: Create a User
          operationId: postApiV2Users
          requestBody:
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    displayName:
                      type: string
                      description: The display name of the user.
                    email:
                      type: string
                      description: The email address of the user.
                    restoreIfDeleted:
                      type: boolean
                      description: Flag to restore user if deleted.
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
    logger.debug("Making POST request to /api/v2/users")
    params = {}
    data = None
    

    

    

    


    
    data = {}

    
    data["displayName"] = body_displayName
    

    
    data["email"] = body_email
    

    
    data["restoreIfDeleted"] = body_restoreIfDeleted
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/users",
        method="POST",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
