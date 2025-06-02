
"""Tools for /mgmt/v1/rbac/users operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def rbacusercontrollerv1_getall() -> Dict[str, Any]:
    '''
    Fetches all RBAC users from the management API.

    Args:
        None

    Returns:
        Dict[str, Any]: The JSON response from the API call containing user details.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      get:
        summary: Retrieve all RBAC users
        operationId: rbacusercontrollerv1_getall
        responses:
          '200':
            description: A list of RBAC users
            content:
              application/json:
                schema:
                  type: object
                  additionalProperties:
                    type: object
          '400':
            description: Bad Request
          '401':
            description: Unauthorized
          '500':
            description: Internal Server Error
    '''
    logger.debug("Making GET request to /mgmt/v1/rbac/users")
    params = {}
    data = None
    


    
    data = {}

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/users",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
