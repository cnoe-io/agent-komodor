
"""Tools for /api/v2/klaudia/rca/sessions/{id} operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def getklaudiarcaresults(path_id: str) -> Dict[str, Any]:
    '''
    Retrieve RCA investigation results.

    Args:
        path_id (str): The identifier for the RCA investigation path.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing RCA investigation results.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Retrieve RCA investigation results
          operationId: getklaudiarcaresults
          parameters:
            - name: path_id
              in: path
              required: true
              schema:
                type: string
          responses:
            '200':
              description: Successful retrieval of RCA investigation results
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties: true
            '400':
              description: Bad request due to invalid path_id
            '404':
              description: RCA investigation results not found
            '500':
              description: Internal server error
    '''
    logger.debug("Making GET request to /api/v2/klaudia/rca/sessions/{id}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/klaudia/rca/sessions/{path_id}",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
