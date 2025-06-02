
"""Tools for /api/v2/health/risks/{id} operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def gethealthriskdata(path_id: str) -> Dict[str, Any]:
    '''
    Get health risk data.

    Args:
        path_id (str): The identifier for the specific health risk data to retrieve.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing health risk data.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      /api/v2/health/risks/{id}:
        get:
          summary: Get health risk data
          parameters:
            - name: path_id
              in: path
              required: true
              description: The identifier for the specific health risk data to retrieve.
              schema:
                type: string
          responses:
            '200':
              description: Successful response with health risk data
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties: true
            '400':
              description: Bad request
            '404':
              description: Health risk data not found
            '500':
              description: Internal server error
    '''
    logger.debug("Making GET request to /api/v2/health/risks/{id}")
    params = {}
    data = None
    

    


    
    data = {}

    

    if not data:
        data = None
    success, response = await make_api_request(
        f"/api/v2/health/risks/{path_id}",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response


async def updatehealthriskstatus(path_id: str, body_status: str = None) -> Dict[str, Any]:
    '''
    Update the status of a health risk.

    Args:
        path_id (str): The unique identifier for the health risk to be updated.
        body_status (str, optional): The new status to be set for the health risk. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call, containing the updated health risk status.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
      put:
        summary: Update the status of a health risk.
        parameters:
          - name: path_id
            in: path
            required: true
            description: The unique identifier for the health risk.
            schema:
              type: string
          - name: body_status
            in: body
            required: false
            description: The new status for the health risk.
            schema:
              type: string
        responses:
          '200':
            description: Successful update of health risk status.
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    status:
                      type: string
          '400':
            description: Bad request due to invalid input.
          '404':
            description: Health risk not found.
          '500':
            description: Internal server error.
    '''
    logger.debug("Making PUT request to /api/v2/health/risks/{id}")
    params = {}
    data = None
    

    

    


    
    data = {}

    

    
    data["status"] = body_status
    

    if not data:
        data = None
    success, response = await make_api_request(
        f"/api/v2/health/risks/{path_id}",
        method="PUT",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
