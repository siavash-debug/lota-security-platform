# Base Connector Contract

All connectors in LOTA Security Verity must implement this standard contract.

---

## 1. Lifecycle Methods

```python
class BaseConnector(ABC):
    @abstractmethod
    async def validate_credentials(self) -> bool:
        """Validate connectivity and authentication without retrieving data."""
        pass

    @abstractmethod
    async def collect_posture(self) -> dict[str, Any]:
        """Collect and return raw posture telemetry in read-only mode."""
        pass

    @abstractmethod
    def normalize(self, raw_data: dict[str, Any]) -> dict[str, Any]:
        """Transform raw posture data into the standard scan input schema."""
        pass
```

---

## 2. Invariants

- **Timeout Boundaries**: No network call may block longer than 30 seconds.
- **Redaction Mandate**: If an external API returns a secret token in an error message, the connector must sanitize the payload before returning.
- **Fail-Safe**: If an integration fails, the connector must emit a structured diagnostic event without failing the entire platform.
