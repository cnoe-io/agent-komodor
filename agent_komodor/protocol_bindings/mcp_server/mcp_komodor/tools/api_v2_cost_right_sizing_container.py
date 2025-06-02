
"""Tools for /api/v2/cost/right-sizing/container operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def getcostrightsizingpercontainer(param_clusterName: str, param_namespace: str, param_serviceKind: str, param_serviceName: str) -> Dict[str, Any]:
    '''
    Get cost right-sizing summary per container.

    Args:
        param_clusterName (str): The name of the cluster.
        param_namespace (str): The namespace within the cluster.
        param_serviceKind (str): The kind of service (e.g., Deployment, StatefulSet).
        param_serviceName (str): The name of the service.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing cost right-sizing information.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Get cost right-sizing summary per container.
          operationId: getCostRightSizingPerContainer
          parameters:
            - name: param_clusterName
              in: query
              required: true
              schema:
                type: string
              description: The name of the cluster.
            - name: param_namespace
              in: query
              required: true
              schema:
                type: string
              description: The namespace within the cluster.
            - name: param_serviceKind
              in: query
              required: true
              schema:
                type: string
              description: The kind of service (e.g., Deployment, StatefulSet).
            - name: param_serviceName
              in: query
              required: true
              schema:
                type: string
              description: The name of the service.
          responses:
            '200':
              description: Successful response containing cost right-sizing information.
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
    logger.debug("Making GET request to /api/v2/cost/right-sizing/container")
    params = {}
    data = None
    

    
    params["clusterName"] = param_clusterName
    

    
    params["namespace"] = param_namespace
    

    
    params["serviceKind"] = param_serviceKind
    

    
    params["serviceName"] = param_serviceName
    


    
    data = {}

    

    

    

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/cost/right-sizing/container",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
