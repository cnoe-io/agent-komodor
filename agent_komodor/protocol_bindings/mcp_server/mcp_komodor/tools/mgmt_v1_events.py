
"""Tools for /mgmt/v1/events operations"""

import logging
from typing import Dict, Any, List
from mcp_komodor.api.client import make_api_request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("mcp_tools")


async def eventscontroller_createcustomevent(body_eventType: str, body_summary: str, body_scope_clusters: List[str] = None, body_scope_servicesNames: List[str] = None, body_scope_namespaces: List[str] = None, body_severity: str = None, body_details: Dict[str, Any] = None) -> Dict[str, Any]:
    '''
    Creates a custom event in the events controller.

    Args:
        body_eventType (str): The type of the event to be created.
        body_summary (str): A brief summary of the event.
        body_scope_clusters (List[str], optional): A list of cluster identifiers that the event is scoped to. Defaults to None.
        body_scope_servicesNames (List[str], optional): A list of service names that the event is scoped to. Defaults to None.
        body_scope_namespaces (List[str], optional): A list of namespaces that the event is scoped to. Defaults to None.
        body_severity (str, optional): The severity level of the event. Defaults to None.
        body_details (Dict[str, Any], optional): Additional details about the event. Defaults to None.

    Returns:
        Dict[str, Any]: The JSON response from the API call.

    Raises:
        Exception: If the API request fails or returns an error.

    OpenAPI Specification:
        post:
          summary: Create a custom event
          operationId: eventscontroller_createcustomevent
          requestBody:
            content:
              application/json:
                schema:
                  type: object
                  properties:
                    eventType:
                      type: string
                    summary:
                      type: string
                    scope_clusters:
                      type: array
                      items:
                        type: string
                    scope_servicesNames:
                      type: array
                      items:
                        type: string
                    scope_namespaces:
                      type: array
                      items:
                        type: string
                    severity:
                      type: string
                    details:
                      type: object
          responses:
            '200':
              description: Successful response
              content:
                application/json:
                  schema:
                    type: object
    '''
    logger.debug("Making POST request to /mgmt/v1/events")
    params = {}
    data = None
    

    

    

    

    

    

    

    


    
    data = {}

    
    data["eventType"] = body_eventType
    

    
    data["summary"] = body_summary
    

    
    data["scope_clusters"] = body_scope_clusters
    

    
    data["scope_servicesNames"] = body_scope_servicesNames
    

    
    data["scope_namespaces"] = body_scope_namespaces
    

    
    data["severity"] = body_severity
    

    
    data["details"] = body_details
    

    if not data:
        data = None
    success, response = await make_api_request(
        "/mgmt/v1/events",
        method="POST",
        params=params,
        data=data
    )
    if not success:
        logger.error(f"Request failed: {response.get('error')}")
        return {"error": response.get('error', 'Request failed')}
    return response
