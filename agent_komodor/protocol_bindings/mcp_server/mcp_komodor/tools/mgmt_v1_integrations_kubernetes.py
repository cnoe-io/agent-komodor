
"""Tools for /mgmt/v1/integrations/kubernetes operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def clustercontroller_post(body_clusterName: str) -> Dict[str, Any]:
    '''
    Posts a new cluster configuration to the Kubernetes integration endpoint.

    Args:
        body_clusterName (str): The name of the cluster to be configured.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing the result of the operation.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      post:
        summary: Create a new Kubernetes cluster configuration
        operationId: clustercontroller_post
        requestBody:
          content:
            application/json:
              schema:
                type: object
                properties:
                  clusterName:
                    type: string
                    description: The name of the cluster to be configured.
                required:
                  - clusterName
        responses:
          '200':
            description: Successful operation
            content:
              application/json:
                schema:
                  type: object
                  additionalProperties: true
          '400':
            description: Bad request
          '500':
            description: Internal server error
    '''
    logger.debug("Making POST request to /mgmt/v1/integrations/kubernetes")
    params = {}
    data = None
    

    


    
    data = {}

    
    data["clusterName"] = body_clusterName
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/integrations/kubernetes",
        method="POST",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
