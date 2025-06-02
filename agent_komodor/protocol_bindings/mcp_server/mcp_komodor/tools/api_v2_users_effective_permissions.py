
"""Tools for /api/v2/users/effective-permissions operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def get_api_v2_users_effective_permissions(param_id: str = None, param_email: str = None) -> Dict[str, Any]:
    '''
    Get User's Effective Permissions.

    Args:
        param_id (str, optional): The user ID to query effective permissions for. Defaults to None.
        param_email (str, optional): The user email to query effective permissions for. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response containing the user's effective permissions.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        paths:
          /api/v2/users/effective-permissions:
            get:
              summary: Get user's effective permissions by either user id or email.
              parameters:
                - name: id
                  in: query
                  required: false
                  description: The user ID to query effective permissions for.
                  schema:
                    type: string
                - name: email
                  in: query
                  required: false
                  description: The user email to query effective permissions for.
                  schema:
                    type: string
              responses:
                '200':
                  description: Successful response containing user's effective permissions.
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
    logger.debug("Making GET request to /api/v2/users/effective-permissions")
    params = {}
    data = None
    

    
    params["id"] = param_id
    

    
    params["email"] = param_email
    


    
    data = {}

    

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/users/effective-permissions",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
