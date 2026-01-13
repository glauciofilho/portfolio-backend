import os
import json
from functools import lru_cache
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.oauth2.service_account import Credentials


@lru_cache
def get_ga_client():
    """
    Cria e cacheia o cliente do Google Analytics
    usando credenciais vindas do .env
    """

    credentials_json = os.getenv("GA_CREDENTIALS_JSON")
    property_id = os.getenv("GA_PROPERTY_ID")

    if not credentials_json:
        raise ValueError("GA_CREDENTIALS_JSON não definido no .env")

    if not property_id:
        raise ValueError("GA_PROPERTY_ID não definido no .env")

    try:
        credentials_info = json.loads(credentials_json)
    except json.JSONDecodeError:
        raise ValueError("GA_CREDENTIALS_JSON inválido (JSON mal formatado)")

    credentials = Credentials.from_service_account_info(credentials_info)

    client = BetaAnalyticsDataClient(credentials=credentials)

    return client, property_id