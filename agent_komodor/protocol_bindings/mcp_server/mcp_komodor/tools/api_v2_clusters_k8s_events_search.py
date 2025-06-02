
"""Tools for /api/v2/clusters/k8s-events/search operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def post_api_v2_clusters_k8s_events_search(body: str) -> Dict[str, Any]:
    '''
    Search for Kubernetes events within a cluster scope.

    This function allows you to search for Kubernetes events based on the provided criteria. The maximum time range for the search is 2 days. If no time range is specified, the default search period is the last 24 hours. The maximum time back for the search is 7 days.

    Args:
        body (str): The request body containing search criteria for Kubernetes events.

    Returns:
        Dict[str, Any]: A dictionary containing the JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        post:
          summary: Search for Kubernetes events in cluster scope.
          description: Search for events based on the provided criteria. Maximum time range is 2 days. If no time range is provided, the default is the last 24 hours. Maximum time back is 7 days.
          operationId: postApiV2ClustersK8sEventsSearch
          requestBody:
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    criteria:
                      type: string
                      description: Criteria for searching events.
          responses:
            '200':
              description: Successful response containing the search results.
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties: true
            '400':
              description: Bad request due to invalid parameters.
            '500':
              description: Internal server error.
    '''
    logger.debug("Making POST request to /api/v2/clusters/k8s-events/search")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/clusters/k8s-events/search",
        method="POST",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
