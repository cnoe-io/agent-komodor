
"""Tools for /mgmt/v1/rbac/actions/{action} operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def actionscontrollerv1_get(path_action: str) -> Dict[str, Any]:
    '''
    Fetches the details of a specific action from the RBAC management API.

    Args:
        path_action (str): The identifier for the action to be retrieved.

    Returns:
        Dict[str, Any]: The JSON response containing the details of the specified action.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Retrieve details of a specific action
          operationId: actionscontrollerv1_get
          parameters:
            - name: path_action
              in: path
              required: true
              description: The identifier for the action to be retrieved
              schema:
                type: string
          responses:
            '200':
              description: Successful response with action details
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties: true
            '404':
              description: Action not found
            '500':
              description: Internal server error
    '''
    logger.debug("Making GET request to /mgmt/v1/rbac/actions/{action}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/rbac/actions/{path_action}",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
