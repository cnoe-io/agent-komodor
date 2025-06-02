
"""Tools for /mgmt/v1/rbac/roles/{id} operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def rolescontrollerv1_get(path_id: str) -> Dict[str, Any]:
    '''
    Fetches role information from the RBAC management API using the specified path ID.

    Args:
        path_id (str): The identifier for the role to be retrieved.

    Returns:
        Dict[str, Any]: The JSON response containing role details from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      get:
        summary: Retrieve role information by ID
        operationId: rolescontrollerv1_get
        parameters:
          - name: path_id
            in: path
            required: true
            description: The identifier for the role
            schema:
              type: string
        responses:
          200:
            description: Successful response with role details
            content:
              application/json:
                schema:
                  type: object
                  additionalProperties: true
          404:
            description: Role not found
          500:
            description: Internal server error
    '''
    logger.debug("Making GET request to /mgmt/v1/rbac/roles/{id}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        f"/mgmt/v1/rbac/roles/{path_id}",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
