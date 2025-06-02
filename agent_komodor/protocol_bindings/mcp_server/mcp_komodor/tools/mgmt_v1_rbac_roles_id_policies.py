
"""Tools for /mgmt/v1/rbac/roles/{id}/policies operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def rbacrolepoliciescontrollerv1_get(path_id: str) -> Dict[str, Any]:
    '''
    Fetches the policies associated with a specific RBAC role.

    Args:
        path_id (str): The unique identifier for the RBAC role.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing the policies.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      get:
        summary: Retrieve policies for a specific RBAC role.
        operationId: rbacrolepoliciescontrollerv1_get
        parameters:
          - name: path_id
            in: path
            required: true
            description: The unique identifier for the RBAC role.
            schema:
              type: string
        responses:
          '200':
            description: A list of policies associated with the RBAC role.
            content:
              application/json:
                schema:
                  type: object
                  additionalProperties:
                    type: object
          '404':
            description: Role not found.
          '500':
            description: Internal server error.
    '''
    logger.debug("Making GET request to /mgmt/v1/rbac/roles/{id}/policies")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        f"/mgmt/v1/rbac/roles/{path_id}/policies",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
