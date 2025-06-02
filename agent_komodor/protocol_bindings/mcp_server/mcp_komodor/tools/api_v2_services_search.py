
"""Tools for /api/v2/services/search operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def post_api_v2_services_search(body_scope: Dict[str, Any] = None, body_kind: List[str] = None, body_status: str = None, body_issueReasonCategory: List[str] = None, body_latestDeployStatus: str = None, body_pagination: Dict[str, Any] = None) -> Dict[str, Any]:
    '''
    Search for services.

    Args:
        body_scope (Dict[str, Any], optional): The scope of the services to search for. Defaults to None.
        body_kind (List[str], optional): The kinds of services to include in the search. Defaults to None.
        body_status (str, optional): The status of the services to search for. Defaults to None.
        body_issueReasonCategory (List[str], optional): The issue reason categories to filter services by. Defaults to None.
        body_latestDeployStatus (str, optional): The latest deployment status to filter services by. Defaults to None.
        body_pagination (Dict[str, Any], optional): Pagination details for the search results. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing the search results.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        post:
          summary: Search for services based on the provided criteria.
          description: If no criteria is provided, the default is to return all services.
          requestBody:
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    scope:
                      type: object
                      additionalProperties: true
                    kind:
                      type: array
                      items:
                        type: string
                    status:
                      type: string
                    issueReasonCategory:
                      type: array
                      items:
                        type: string
                    latestDeployStatus:
                      type: string
                    pagination:
                      type: object
                      additionalProperties: true
          responses:
            '200':
              description: Successful response with the list of services.
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties: true
            '400':
              description: Bad request due to invalid input.
            '500':
              description: Internal server error.
    '''
    logger.debug("Making POST request to /api/v2/services/search")
    params = {}
    data = None
    

    

    

    

    

    

    


    
    data = {}

    
    data["scope"] = body_scope
    

    
    data["kind"] = body_kind
    

    
    data["status"] = body_status
    

    
    data["issueReasonCategory"] = body_issueReasonCategory
    

    
    data["latestDeployStatus"] = body_latestDeployStatus
    

    
    data["pagination"] = body_pagination
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/services/search",
        method="POST",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
