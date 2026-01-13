from google.analytics.data_v1beta.types import (RunReportRequest, DateRange, Metric, Dimension)
from .ga_service import get_ga_client

def get_overview():
    client, property_id = get_ga_client()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
        metrics=[
            Metric(name="activeUsers"),
            Metric(name="eventCount"),
            Metric(name="screenPageViews"),
        ],
    )

    response = client.run_report(request)

    if not response.rows:
        return {
            "users": 0,
            "events": 0,
            "page_views": 0,
        }

    row = response.rows[0]

    return {
        "users": int(row.metric_values[0].value),
        "events": int(row.metric_values[1].value),
        "page_views": int(row.metric_values[2].value),
    }

def get_countries():
    client, property_id = get_ga_client()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
        dimensions=[Dimension(name="country")],
        metrics=[Metric(name="activeUsers")],
        order_bys=[],
    )

    response = client.run_report(request)

    countries = []

    for row in response.rows:
        countries.append({
            "country": row.dimension_values[0].value,
            "total": int(row.metric_values[0].value),
        })

    return countries

def get_project_events():
    client, property_id = get_ga_client()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
        dimensions=[Dimension(name="customEvent:project_id")],
        metrics=[Metric(name="eventCount")],
    )

    response = client.run_report(request)

    projects = []

    for row in response.rows:
        projects.append({
            "project_id": row.dimension_values[0].value,
            "total": int(row.metric_values[0].value),
        })

    return projects