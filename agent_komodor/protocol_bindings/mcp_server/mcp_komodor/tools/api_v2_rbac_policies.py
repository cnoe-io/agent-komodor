
"""Tools for /api/v2/rbac/policies operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def post_api_v2_rbac_policies(body_name: str, body_statements: List[str]) -> Dict[str, Any]:
    '''
    Create a new RBAC policy.

    Args:
        body_name (str): The name of the policy to be created.
        body_statements (List[str]): A list of statements defining the policy rules.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing details of the created policy.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        post:
          summary: Create a new RBAC policy
          operationId: postApiV2RbacPolicies
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    name:
                      type: string
                      description: The name of the policy.
                    statements:
                      type: array
                      items:
                        type: string
                      description: The policy statements.
          responses:
            '200':
              description: Successful response
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      id:
                        type: string
                        description: The ID of the created policy.
                      name:
                        type: string
                        description: The name of the created policy.
                      statements:
                        type: array
                        items:
                          type: string
                        description: The statements of the created policy.
            '400':
              description: Bad Request
            '500':
              description: Internal Server Error
    '''
    logger.debug("Making POST request to /api/v2/rbac/policies")
    params = {}
    data = None
    

    

    


    
    data = {}

    
    data["name"] = body_name
    

    
    data["statements"] = body_statements
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/rbac/policies",
        method="POST",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
