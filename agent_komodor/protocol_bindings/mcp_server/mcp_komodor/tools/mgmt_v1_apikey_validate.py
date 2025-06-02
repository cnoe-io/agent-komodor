
"""Tools for /mgmt/v1/apikey/validate operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def apikeyscontroller_validate() -> Dict[str, Any]:
    '''
    Validates the API key by making a GET request to the validation endpoint.

    Args:
        None

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing validation results.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Validate API Key
          description: Validates the API key by making a GET request to the validation endpoint.
          operationId: apikeyscontroller_validate
          responses:
            '200':
              description: Successful validation of the API key.
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      valid:
                        type: boolean
                        description: Indicates if the API key is valid.
                      message:
                        type: string
                        description: Additional information about the validation result.
            '400':
              description: Bad Request if the validation fails due to client error.
            '500':
              description: Internal Server Error if the server encounters an unexpected condition.
    '''
    logger.debug("Making GET request to /mgmt/v1/apikey/validate")
    params = {}
    data = None
    


    
    data = {}

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/apikey/validate",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
