
"""Tools for /api/v2/klaudia/rca/sessions operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def triggerklaudiarca(body_kind: str, body_name: str, body_namespace: str, body_clusterName: str) -> Dict[str, Any]:
    '''
    Trigger a new RCA investigation.

    Args:
        body_kind (str): The kind of the resource to investigate.
        body_name (str): The name of the resource to investigate.
        body_namespace (str): The namespace of the resource to investigate.
        body_clusterName (str): The name of the cluster where the resource is located.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      post:
        summary: Trigger a new RCA investigation
        operationId: triggerklaudiarca
        requestBody:
          content:
            application/json:
              schema:
                type: object
                properties:
                  kind:
                    type: string
                    description: The kind of the resource to investigate.
                  name:
                    type: string
                    description: The name of the resource to investigate.
                  namespace:
                    type: string
                    description: The namespace of the resource to investigate.
                  clusterName:
                    type: string
                    description: The name of the cluster where the resource is located.
                required:
                  - kind
                  - name
                  - namespace
                  - clusterName
        responses:
          '200':
            description: Successful response
            content:
              application/json:
                schema:
                  type: object
          '400':
            description: Bad request
          '500':
            description: Internal server error
    '''
    logger.debug("Making POST request to /api/v2/klaudia/rca/sessions")
    params = {}
    data = None
    

    

    

    

    


    
    data = {}

    
    data["kind"] = body_kind
    

    
    data["name"] = body_name
    

    
    data["namespace"] = body_namespace
    

    
    data["clusterName"] = body_clusterName
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/klaudia/rca/sessions",
        method="POST",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
