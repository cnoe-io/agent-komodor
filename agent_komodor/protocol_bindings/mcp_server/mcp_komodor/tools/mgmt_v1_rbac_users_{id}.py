
"""Tools for /mgmt/v1/rbac/users/{id} operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def rbacusercontrollerv1_get(path_id: str) -> Dict[str, Any]:
    '''
    Fetches RBAC user details for a given user ID.

    Args:
        path_id (str): The user ID to fetch details for.

    Returns:
        Dict[str, Any]: The JSON response containing user details.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      get:
        summary: Fetch RBAC user details
        operationId: rbacusercontrollerv1_get
        parameters:
          - name: path_id
            in: path
            required: true
            description: The user ID to fetch details for
            schema:
              type: string
        responses:
          200:
            description: Successful response
            content:
              application/json:
                schema:
                  type: object
                  additionalProperties: true
          404:
            description: User not found
          500:
            description: Internal server error
    '''
    logger.debug("Making GET request to /mgmt/v1/rbac/users/{id}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/users/{path_id}",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
