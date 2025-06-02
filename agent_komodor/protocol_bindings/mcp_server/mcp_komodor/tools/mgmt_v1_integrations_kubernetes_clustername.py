
"""Tools for /mgmt/v1/integrations/kubernetes/{clusterName} operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def clustercontroller_getbyclustername(path_clusterName: str) -> Dict[str, Any]:
    '''
    Fetches the cluster details by cluster name.

    Args:
        path_clusterName (str): The name of the cluster to retrieve details for.

    Returns:
        Dict[str, Any]: The JSON response containing cluster details.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      get:
        summary: Retrieve cluster details by cluster name
        operationId: clustercontroller_getbyclustername
        parameters:
          - name: clusterName
            in: path
            required: true
            description: The name of the cluster
            schema:
              type: string
        responses:
          200:
            description: Successful response containing cluster details
            content:
              application/json:
                schema:
                  type: object
                  additionalProperties: true
          default:
            description: Error response
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    error:
                      type: string
    '''
    logger.debug("Making GET request to /mgmt/v1/integrations/kubernetes/{clusterName}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        f"/mgmt/v1/integrations/kubernetes/{path_clusterName}",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
