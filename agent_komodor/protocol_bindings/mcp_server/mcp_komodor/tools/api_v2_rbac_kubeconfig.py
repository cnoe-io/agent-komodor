
"""Tools for /api/v2/rbac/kubeconfig operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def get_api_v2_rbac_kubeconfig(param_clusterName: List[str] = None) -> Dict[str, Any]:
    '''
    Download Kubeconfig File.

    Args:
        param_clusterName (List[str], optional): A list of cluster names for which to download the kubeconfig file. Defaults to None, which will return the kubeconfig file for all available clusters.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing the kubeconfig file data.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Download Kubeconfig File
          description: Download a kubeconfig file for the specified cluster names. If no cluster names are specified, the kubeconfig file for all available clusters will be returned.
          parameters:
            - name: param_clusterName
              in: query
              description: A list of cluster names for which to download the kubeconfig file.
              required: false
              schema:
                type: array
                items:
                  type: string
          responses:
            '200':
              description: Successful response containing the kubeconfig file data.
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
    logger.debug("Making GET request to /api/v2/rbac/kubeconfig")
    params = {}
    data = None
    

    
    params["clusterName"] = param_clusterName
    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/rbac/kubeconfig",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
