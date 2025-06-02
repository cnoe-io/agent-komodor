
"""Tools for /mgmt/v1/integrations/kubernetes/{id} operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def clustercontroller_delete(path_id: str) -> Dict[str, Any]:
    '''
    Deletes a Kubernetes integration by its path ID.

    Args:
        path_id (str): The unique identifier for the Kubernetes integration to be deleted.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing the result of the delete operation.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        delete:
          summary: Delete a Kubernetes integration
          operationId: clustercontroller_delete
          parameters:
            - name: path_id
              in: path
              required: true
              description: The unique identifier for the Kubernetes integration
              schema:
                type: string
          responses:
            '200':
              description: Successful deletion
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties: true
            '404':
              description: Integration not found
            '500':
              description: Server error
    '''
    logger.debug("Making DELETE request to /mgmt/v1/integrations/kubernetes/{id}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/integrations/kubernetes/{path_id}",
        method="DELETE",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
