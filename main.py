# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""
#USSD Canal plus menu manager functions coverage tests

This code is a set of unit tests written using the `unittest` framework in Python. It tests the behavior of several functions related to a USSD (Unstructured Supplementary Service Data) service that deals with paying TV bills. The code uses mocking to simulate the behavior of certain components and functions without actually invoking them, which is useful for testing purposes.

Here’s a breakdown of each part:

### Imports

```python
import unittest
from unittest.mock import MagicMock, patch
from ussd_core.functions.pay.bill import (get_tv_billers, get_biller_details,
                                          bill_enquiry, validate_bill, pay_tv_subscription)
```

1. **`unittest`**: A built-in Python module used for creating and running tests.
2. **`unittest.mock.MagicMock`**: A class used to create mock objects, which can simulate the behavior of real objects in tests.
3. **`unittest.mock.patch`**: A decorator used to temporarily replace the targeted object with a mock object during a test.
4. **`from ussd_core.functions.pay.bill import ...`**: Imports specific functions from the `bill` module, which are the ones being tested.

### Class and Setup

```python
class TestBillerFunctions(unittest.TestCase):
    def setUp(self):
        self.settings = MagicMock()
        self.ussd_request = MagicMock()
        self.ussd_request.telco = "telco"
        self.ussd_request.session_id = "TvSession243"
        self.ussd_request.language = 'en'
        self.ussd_request.session = {'country_code': '243', 'service_code': '123456789'}
```

1. **`TestBillerFunctions(unittest.TestCase)`**: Defines a test class that inherits from `unittest.TestCase`, making it a test case that can be run by the `unittest` framework.
2. **`setUp(self)`**: A special method in `unittest` that runs before each test method. It’s used to set up any necessary objects or state.
   - **`self.settings = MagicMock()`**: Creates a mock object named `settings`, simulating any settings that might be needed.
   - **`self.ussd_request = MagicMock()`**: Creates a mock object named `ussd_request`, simulating a USSD request object.
   - **`self.ussd_request.telco = "telco"`**: Sets an attribute `telco` on the `ussd_request` mock object.
   - **`self.ussd_request.session_id = "TvSession243"`**: Sets the session ID of the USSD request.
   - **`self.ussd_request.language = 'en'`**: Sets the language of the USSD request.
   - **`self.ussd_request.session = {...}`**: Sets the session data, including the country code and service code.

### Test Methods

#### `test_get_tv_billers`

```python
@patch("ussd_core.service_layer_callers.callers.V1ServiceLayerCallerClientToken")
def test_get_tv_billers(self, mock_caller_class):
    mock_caller = mock_caller_class.return_value
    get_tv_billers(self.ussd_request)
    mocked_ussd_request_object = {"category": "Utilities"}
    mock_caller_class.assert_called_once_with(
        ussd_request=self.ussd_request,
        request_body=mocked_ussd_request_object,
        auto_token_add=True,
    )
    mock_caller.add_country_code.assert_called_once_with("CountryCode")
    mock_caller.get_response.assert_called()
```

1. **`@patch("...V1ServiceLayerCallerClientToken")`**: Temporarily replaces the `V1ServiceLayerCallerClientToken` class with a mock object.
2. **`def test_get_tv_billers(self, mock_caller_class):`**: Defines a test method that takes `mock_caller_class` as an argument, which is the mock version of `V1ServiceLayerCallerClientToken`.
   - **`mock_caller = mock_caller_class.return_value`**: Gets the mock object that would be returned if `V1ServiceLayerCallerClientToken` were instantiated.
   - **`get_tv_billers(self.ussd_request)`**: Calls the `get_tv_billers` function with the mocked `ussd_request`.
   - **`mocked_ussd_request_object = {"category": "Utilities"}`**: Defines what the request body should look like.
   - **`mock_caller_class.assert_called_once_with(...)`**: Asserts that `V1ServiceLayerCallerClientToken` was called exactly once with the expected arguments.
   - **`mock_caller.add_country_code.assert_called_once_with("CountryCode")`**: Asserts that `add_country_code` was called once with "CountryCode".
   - **`mock_caller.get_response.assert_called()`**: Asserts that `get_response` was called.

#### `test_get_biller_details`

```python
@patch('ussd_core.service_layer_callers.callers.V1ServiceLayerCallerClientToken')
@patch("ussd_core.functions.pay.bill.fetch_session_data")
def test_get_biller_details(self, mock_caller_class, mocked_fetch_session_data):
    mock_caller = mock_caller_class.return_value
    get_biller_details(self.ussd_request)
    mocked_ussd_request_object = {'biller_code': mocked_fetch_session_data(self.ussd_request, 'biller.billerCode')}
    mock_caller_class.assert_called_once_with(
        ussd_request=self.ussd_request,
        request_body=mocked_ussd_request_object,
        auto_token_add=False,
    )
    mock_caller.add_country_code.assert_called()
    mock_caller.add_msisdn_from_request.assert_called()
    mock_caller.get_response.assert_called()
```

1. **`@patch('...fetch_session_data')`**: Also mocks the `fetch_session_data` function.
2. **`def test_get_biller_details(self, mock_caller_class, mocked_fetch_session_data):`**: Adds `mocked_fetch_session_data`, a mock version of `fetch_session_data`, to the arguments.
   - **`mocked_ussd_request_object = {...}`**: The request body is set to include the biller code, fetched using the mocked `fetch_session_data`.
   - **`mock_caller.add_msisdn_from_request.assert_called()`**: Additionally asserts that the `add_msisdn_from_request` method was called on `mock_caller`.

#### `test_bill_enquiry`

```python
@patch('ussd_core.service_layer_callers.callers.V1ServiceLayerCallerClientToken')
@patch("ussd_core.functions.pay.bill.fetch_session_data")
def test_bill_enquiry(self, mock_caller_class, mocked_fetch_session_data):
    mock_caller = mock_caller_class.return_value
    bill_enquiry(self.ussd_request)
    mocked_ussd_request_object = {
        "CardNumber": mocked_fetch_session_data(self.ussd_request, 'biller_reference'),
        "OperationType": mocked_fetch_session_data(self.ussd_request, 'operation_type'),
        "Currency": mocked_fetch_session_data(self.ussd_request, 'biller.response.currencyCode'),
        "Reference": mocked_fetch_session_data(self.ussd_request, 'biller_reference')
    }
    mock_caller_class.assert_called_once_with(
        ussd_request=self.ussd_request,
        request_body=mocked_ussd_request_object,
        auto_token_add=False,
    )
    mock_caller.add_country_code.assert_called_once_with("CountryCode")
    mock_caller.get_response.assert_called()
```

1. **`def test_bill_enquiry(self, mock_caller_class, mocked_fetch_session_data):`**: This test method tests the `bill_enquiry` function.
   - **`mocked_ussd_request_object = {...}`**: The request body is populated with several pieces of data fetched via `mocked_fetch_session_data`.
   - **`mock_caller_class.assert_called_once_with(...)`**: Asserts that the correct request body was passed to `V1ServiceLayerCallerClientToken`.
   - **`mock_caller.add_country_code.assert_called_once_with("CountryCode")`**: Asserts that the country code was added.
   - **`mock_caller.get_response.assert_called()`**: Asserts that `get_response` was called.

### Overall Purpose

The overall purpose of this code is to test various functions (`get_tv_billers`, `get_biller_details`, `bill_enquiry`) related to handling TV bill payments in a USSD application. The tests ensure that the functions interact correctly with other components, such as the USSD request object and service layer caller, by verifying that the appropriate methods are called with the correct arguments. The use of mocking allows these tests to be run in isolation, without depending on external systems or data.



"""
