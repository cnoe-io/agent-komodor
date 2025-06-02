
"""Tools for /api/v2/cost/allocation operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def getcostallocation(param_timeFrame: str, param_groupBy: str, param_pageSize: int, param_clusterScope: List[str] = None, param_filterBy: str = None, param_filterValueEquals: str = None, param_sortOrder: str = None, param_sortBy: str = None) -> Dict[str, Any]:
    '''
    Get cost allocation breakdown.

    Args:
        param_timeFrame (str): The time frame for the cost allocation data.
        param_groupBy (str): The parameter to group the cost allocation data by.
        param_pageSize (int): The number of records to return per page.
        param_clusterScope (List[str], optional): The scope of clusters to include in the cost allocation. Defaults to None.
        param_filterBy (str, optional): The field to filter the cost allocation data by. Defaults to None.
        param_filterValueEquals (str, optional): The value to filter the cost allocation data by. Defaults to None.
        param_sortOrder (str, optional): The order to sort the cost allocation data. Defaults to None.
        param_sortBy (str, optional): The field to sort the cost allocation data by. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing the cost allocation breakdown.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        get:
          summary: Retrieve a breakdown of cost allocation across clusters, workspaces, or any user-defined grouping.
          parameters:
            - name: param_timeFrame
              in: query
              required: true
              description: The time frame for the cost allocation data.
              schema:
                type: string
            - name: param_groupBy
              in: query
              required: true
              description: The parameter to group the cost allocation data by.
              schema:
                type: string
            - name: param_pageSize
              in: query
              required: true
              description: The number of records to return per page.
              schema:
                type: integer
            - name: param_clusterScope
              in: query
              required: false
              description: The scope of clusters to include in the cost allocation.
              schema:
                type: array
                items:
                  type: string
            - name: param_filterBy
              in: query
              required: false
              description: The field to filter the cost allocation data by.
              schema:
                type: string
            - name: param_filterValueEquals
              in: query
              required: false
              description: The value to filter the cost allocation data by.
              schema:
                type: string
            - name: param_sortOrder
              in: query
              required: false
              description: The order to sort the cost allocation data.
              schema:
                type: string
            - name: param_sortBy
              in: query
              required: false
              description: The field to sort the cost allocation data by.
              schema:
                type: string
          responses:
            '200':
              description: Successful response containing the cost allocation breakdown.
              content:
                application/json:
                  schema:
                    type: object
    '''
    logger.debug("Making GET request to /api/v2/cost/allocation")
    params = {}
    data = None
    

    
    params["timeFrame"] = param_timeFrame
    

    
    params["groupBy"] = param_groupBy
    

    
    params["pageSize"] = param_pageSize
    

    
    params["clusterScope"] = param_clusterScope
    

    
    params["filterBy"] = param_filterBy
    

    
    params["filterValueEquals"] = param_filterValueEquals
    

    
    params["sortOrder"] = param_sortOrder
    

    
    params["sortBy"] = param_sortBy
    


    
    data = {}

    

    

    

    

    

    

    

    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/cost/allocation",
        method="GET",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
