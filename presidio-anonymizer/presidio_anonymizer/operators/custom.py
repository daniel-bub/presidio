"""Replaces the PII text with lambda result."""
from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType
from presidio_anonymizer.services.validators import validate_type
from presidio_anonymizer.entities import InvalidParamException


class Custom(Operator):
    """
    Replace PII text entity with the lambda result executed on the PII text.

    lambda retrun type must be a string
    If the new value is not a lambda, this will act as a replace method
    """

    NEW_VALUE = "new_value"

    def operate(self, text: str = None, params: Dict = None) -> str:
        """:return: new_value."""
        new_val = params.get(self.NEW_VALUE)
        if not new_val:
            return f"<{params.get('entity_type')}>"
        return new_val(text) if callable(new_val) else new_val

    def validate(self, params: Dict = None) -> None:
        """Validate the new value is string."""
        new_val = params.get(self.NEW_VALUE)
        if callable(new_val):
            if (type(new_val("PII")) == str):
                return
            else:
                raise InvalidParamException("Invalid method return type. must be a str")
        else:
            validate_type(new_val, self.NEW_VALUE, str)
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "custom"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize