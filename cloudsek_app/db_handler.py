import uuid
import json
from .constants import NUMBER1, NUMBER2, TOTAL, ID_PK


def build_payload_and_calculate(self, body):
    total = body.get(NUMBER1) + body.get(NUMBER2)
    id  = uuid.uuid4().hex
    body[ID_PK] = id
    body[TOTAL] = total
    return body