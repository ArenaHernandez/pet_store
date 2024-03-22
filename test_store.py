from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_
import json
import requests

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''

def test_order_schema():
    test_endpoint = "/store/order"
    data = {
      "pet_id": 0
    }

    response = api_helpers.post_api_data(test_endpoint, data=data)

    assert response.status_code == 201

    # Validate the response schema against the defined schema in schemas.py
    validate(instance=response.json(), schema=schemas.order)



@pytest.mark.parametrize("order_id, status_code", [
    ("48b1a535-5c1d-428b-9c24-047394b3af46", 200),  # Assuming 200 is the expected status code
])
def test_patch_order(order_id, status_code):
    endpoint = f"/store/order/{order_id}"

    data = {
        "status": "available"
    }

    response = api_helpers.patch_api_data(endpoint, data=data)
    print("Response:", response.json())  # Print the response received from the server

    assert response.status_code == status_code

