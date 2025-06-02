
"""Tools for /mgmt/v1/rbac/users/{id}/roles operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def rbacuserrolescontrollerv1_get(path_id: str) -> Dict[str, Any]:
    '''
    Fetches the roles associated with a specific user in the RBAC system.

    Args:
        path_id (str): The unique identifier of the user whose roles are to be retrieved.

    Returns:
        Dict[str, Any]: A dictionary containing the JSON response from the API call, which includes the roles of the specified user.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Retrieve roles for a specific user in the RBAC system.
          operationId: rbacuserrolescontrollerv1_get
          parameters:
            - name: path_id
              in: path
              required: true
              description: The unique identifier of the user.
              schema:
                type: string
          responses:
            '200':
              description: A list of roles associated with the user.
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties:
                      type: string
            '404':
              description: User not found.
            '500':
              description: Internal server error.
    '''
    logger.debug("Making GET request to /mgmt/v1/rbac/users/{id}/roles")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/users/{path_id}/roles",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
