
"""Tools for /api/v2/audit-log/filters operations"""

import logging
from typing import Dict, Any
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def get_api_v2_audit_log_filters(param_startTime: str = None, param_endTime: str = None) -> Dict[str, Any]:
    '''
    Get available filter values for Query Audit Logs.

    Args:
        param_startTime (str, optional): The start time for filtering audit logs. Defaults to None.
        param_endTime (str, optional): The end time for filtering audit logs. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing available filter values.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Get available filter values for Query Audit Logs
          operationId: getApiV2AuditLogFilters
          parameters:
            - name: param_startTime
              in: query
              required: false
              description: The start time for filtering audit logs.
              schema:
                type: string
            - name: param_endTime
              in: query
              required: false
              description: The end time for filtering audit logs.
              schema:
                type: string
          responses:
            '200':
              description: Successful response containing filter values.
              content:
                application/json:
                  schema:
                    type: object
                    additionalProperties:
                      type: string
            '400':
              description: Bad request due to invalid parameters.
            '500':
              description: Internal server error.
    '''
    logger.debug("Making GET request to /api/v2/audit-log/filters")
    params = {}
    data = None
    

    
    params["startTime"] = param_startTime
    

    
    params["endTime"] = param_endTime
    


    
    data = {}

    

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/audit-log/filters",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
