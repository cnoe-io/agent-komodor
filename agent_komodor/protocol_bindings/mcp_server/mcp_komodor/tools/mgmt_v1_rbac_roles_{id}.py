
"""Tools for /mgmt/v1/rbac/roles/{id} operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def rolescontrollerv1_get(path_id: str) -> Dict[str, Any]:
    '''
    Fetches role details from the RBAC management API for a given role ID.

    Args:
        path_id (str): The ID of the role to retrieve details for.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing role details.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      get:
        summary: Retrieve role details by ID
        operationId: rolescontrollerv1_get
        parameters:
          - name: path_id
            in: path
            required: true
            description: The ID of the role to retrieve.
            schema:
              type: string
        responses:
          '200':
            description: Successful response with role details.
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    id:
                      type: string
                    name:
                      type: string
                    permissions:
                      type: array
                      items:
                        type: string
          '404':
            description: Role not found.
          '500':
            description: Internal server error.
    '''
    logger.debug("Making GET request to /mgmt/v1/rbac/roles/{id}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/roles/{path_id}",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
