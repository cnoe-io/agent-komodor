
"""Tools for /api/v2/services/issues/search operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def post_api_v2_services_issues_search(body: str) -> Dict[str, Any]:
    '''
    Search for issues in service scope.

    Args:
        body (str): The request body containing search criteria for issues.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing the search results.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      post:
        summary: Search for issues in service scope
        description: Search for issues based on the provided criteria. Maximum time range is 2 days. If no time range is provided, the default is the last 24 hours. Maximum time back is 7 days.
        operationId: post_api_v2_services_issues_search
        requestBody:
          content:
            application/json:
              schema:
                type: string
        responses:
          '200':
            description: Successful response with search results
            content:
              application/json:
                schema:
                  type: object
                  additionalProperties: true
          '400':
            description: Bad request due to invalid input
          '500':
            description: Internal server error
    '''
    logger.debug("Making POST request to /api/v2/services/issues/search")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/services/issues/search",
        method="POST",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
