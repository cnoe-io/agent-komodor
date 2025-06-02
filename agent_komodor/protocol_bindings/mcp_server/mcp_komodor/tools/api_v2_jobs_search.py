
"""Tools for /api/v2/jobs/search operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def post_api_v2_jobs_search(body_scope: Dict[str, Any] = None, body_types: List[str] = None, body_status: str = None, body_pagination: Dict[str, Any] = None) -> Dict[str, Any]:
    '''
    Search for jobs and cron jobs.

    Args:
        body_scope (Dict[str, Any], optional): The scope of the jobs to search for. Defaults to None.
        body_types (List[str], optional): The types of jobs to include in the search. Defaults to None.
        body_status (str, optional): The status of the jobs to filter by. Defaults to None.
        body_pagination (Dict[str, Any], optional): Pagination details for the search results. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call containing the search results.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        post:
          summary: Search for jobs and cron jobs
          description: Search for jobs based on the provided criteria. If no criteria is provided, the default is to return all jobs.
          requestBody:
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    scope:
                      type: object
                      description: The scope of the jobs to search for.
                    types:
                      type: array
                      items:
                        type: string
                      description: The types of jobs to include in the search.
                    status:
                      type: string
                      description: The status of the jobs to filter by.
                    pagination:
                      type: object
                      description: Pagination details for the search results.
          responses:
            '200':
              description: A JSON response containing the search results.
              content:
                application/json:
                  schema:
                    type: object
            '400':
              description: Bad request due to invalid input.
            '500':
              description: Internal server error.
    '''
    logger.debug("Making POST request to /api/v2/jobs/search")
    params = {}
    data = None
    

    

    

    

    


    
    data = {}

    
    data["scope"] = body_scope
    

    
    data["types"] = body_types
    

    
    data["status"] = body_status
    

    
    data["pagination"] = body_pagination
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/api/v2/jobs/search",
        method="POST",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
