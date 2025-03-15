from applicationinsights import TelemetryClient
import time
import sys

# Initialize the telemetry client
instrumentation_key = 'df72d563-8e8e-4c28-b074-817ea925d10b'
tc = TelemetryClient(instrumentation_key)

# Track custom events and metrics
tc.track_event('TestEvent', {'example': 'value'})
tc.track_metric('TestMetric', 100)

# Track a request
tc.track_request('GET /api/values', '/api/values', time.time(), 200, True)

# Track an exception
try:
    1 / 0
except ZeroDivisionError as e:
    tc.track_exception(*sys.exc_info())

# Flush the telemetry data to Azure
tc.flush()

print("Telemetry sent.")

