
"""Tools for /api/v2/service/yaml operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def get_api_v2_service_yaml(param_cluster: str, param_namespace: str, param_kind: str, param_name: str) -> Dict[str, Any]:
    '''
    Get the YAML for a service.

    Args:
        param_cluster (str): The cluster identifier for the service.
        param_namespace (str): The namespace in which the service resides.
        param_kind (str): The kind of the service resource.
        param_name (str): The name of the service.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing the service YAML.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Get the YAML for a service
          parameters:
            - name: param_cluster
              in: query
              required: true
              schema:
                type: string
              description: The cluster identifier for the service.
            - name: param_namespace
              in: query
              required: true
              schema:
                type: string
              description: The namespace in which the service resides.
            - name: param_kind
              in: query
              required: true
              schema:
                type: string
              description: The kind of the service resource.
            - name: param_name
              in: query
              required: true
              schema:
                type: string
              description: The name of the service.
          responses:
            '200':
              description: Successful response with the service YAML.
              content:
                application/json:
                  schema:
                    type: object
            '400':
              description: Bad request due to invalid parameters.
            '500':
              description: Internal server error.
    '''
    logger.debug("Making GET request to /api/v2/service/yaml")
    params = {}
    data = None
    

    
    params["cluster"] = param_cluster
    

    
    params["namespace"] = param_namespace
    

    
    params["kind"] = param_kind
    

    
    params["name"] = param_name
    


    
    data = {}

    

    

    

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/service/yaml",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
