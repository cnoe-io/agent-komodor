
"""Tools for /api/v2/clusters operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def get_api_v2_clusters(param_clusterName: List[str] = None, param_tags: List[str] = None) -> Dict[str, Any]:
    '''
    Get list of clusters.

    Args:
        param_clusterName (List[str], optional): A list of cluster names to filter the results. Defaults to None.
        param_tags (List[str], optional): A list of tags to filter the clusters. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing the list of clusters.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Fetch a list of all clusters, optionally filtered by name or tags.
          parameters:
            - name: param_clusterName
              in: query
              description: A list of cluster names to filter the results.
              required: false
              schema:
                type: array
                items:
                  type: string
            - name: param_tags
              in: query
              description: A list of tags to filter the clusters.
              required: false
              schema:
                type: array
                items:
                  type: string
          responses:
            '200':
              description: A list of clusters.
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties: true
            '400':
              description: Bad request.
            '500':
              description: Internal server error.
    '''
    logger.debug("Making GET request to /api/v2/clusters")
    params = {}
    data = None
    

    
    params["clusterName"] = param_clusterName
    

    
    params["tags"] = param_tags
    


    
    data = {}

    

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/clusters",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
