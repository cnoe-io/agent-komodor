
"""Tools for /api/v2/cost/right-sizing/service operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def getcostrightsizingperservice(param_optimizationStrategy: str, param_pageSize: int, param_filterBy: str = None, param_filterValueEquals: str = None, param_sortOrder: str = None, param_sortBy: str = None, param_clusterScope: List[str] = None) -> Dict[str, Any]:
    '''
    Get cost right-sizing recommendations per service.

    Args:
        param_optimizationStrategy (str): The strategy to use for optimization.
        param_pageSize (int): The number of results to return per page.
        param_filterBy (str, optional): The field to filter results by. Defaults to None.
        param_filterValueEquals (str, optional): The value to filter the field by. Defaults to None.
        param_sortOrder (str, optional): The order to sort results in. Defaults to None.
        param_sortBy (str, optional): The field to sort results by. Defaults to None.
        param_clusterScope (List[str], optional): The scope of clusters to consider. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Get cost right-sizing recommendations per service.
          description: Get recommended CPU and memory request adjustments per service to optimize cost.
          parameters:
            - name: optimizationStrategy
              in: query
              required: true
              schema:
                type: string
            - name: pageSize
              in: query
              required: true
              schema:
                type: integer
            - name: filterBy
              in: query
              required: false
              schema:
                type: string
            - name: filterValueEquals
              in: query
              required: false
              schema:
                type: string
            - name: sortOrder
              in: query
              required: false
              schema:
                type: string
            - name: sortBy
              in: query
              required: false
              schema:
                type: string
            - name: clusterScope
              in: query
              required: false
              schema:
                type: array
                items:
                  type: string
          responses:
            '200':
              description: Successful response with recommendations.
              content:
                application/json:
                  schema:
                    type: object
            '400':
              description: Bad request due to invalid parameters.
            '500':
              description: Internal server error.
    '''
    logger.debug("Making GET request to /api/v2/cost/right-sizing/service")
    params = {}
    data = None
    

    
    params["optimizationStrategy"] = param_optimizationStrategy
    

    
    params["pageSize"] = param_pageSize
    

    
    params["filterBy"] = param_filterBy
    

    
    params["filterValueEquals"] = param_filterValueEquals
    

    
    params["sortOrder"] = param_sortOrder
    

    
    params["sortBy"] = param_sortBy
    

    
    params["clusterScope"] = param_clusterScope
    


    
    data = {}

    

    

    

    

    

    

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/cost/right-sizing/service",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
