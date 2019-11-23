# openapi_client.RegistrationApi

All URIs are relative to *https://secure.tpay.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_gw_api_key_registration_inputs_post**](RegistrationApi.md#api_gw_api_key_registration_inputs_post) | **POST** /api/gw/{api_key}/registration/inputs | inputs
[**api_gw_api_key_registration_register_post**](RegistrationApi.md#api_gw_api_key_registration_register_post) | **POST** /api/gw/{api_key}/registration/register | register


# **api_gw_api_key_registration_inputs_post**
> RegistrationInputsResponse api_gw_api_key_registration_inputs_post(api_key, basic_data=basic_data)

inputs

This method returns branches list and legal forms list which are available in Tpay.com. These data are required to correctly merchant registration. Branch id and legal form id should be sent in register method.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.RegistrationApi()
api_key = 'api_key_example' # str | The api key.
basic_data = openapi_client.RegistrationInputFields() # RegistrationInputFields | Registration inputs. (optional)

try:
    # inputs
    api_response = api_instance.api_gw_api_key_registration_inputs_post(api_key, basic_data=basic_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->api_gw_api_key_registration_inputs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. | 
 **basic_data** | [**RegistrationInputFields**](RegistrationInputFields.md)| Registration inputs. | [optional] 

### Return type

[**RegistrationInputsResponse**](RegistrationInputsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tpay response |  -  |
**403** | Access denied |  -  |
**404** | Invalid api key or password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_gw_api_key_registration_register_post**
> RegistrationRegisterResponse api_gw_api_key_registration_register_post(api_key, registrtation_register_data=registrtation_register_data)

register

This method allows register new account in Tpay.com system. In response, the method returns data which can be used to generate new transactions. Optionally method returns access data for API transactions

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.RegistrationApi()
api_key = 'api_key_example' # str | The api key.
registrtation_register_data = openapi_client.RegisterFields() # RegisterFields | Register data (optional)

try:
    # register
    api_response = api_instance.api_gw_api_key_registration_register_post(api_key, registrtation_register_data=registrtation_register_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->api_gw_api_key_registration_register_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. | 
 **registrtation_register_data** | [**RegisterFields**](RegisterFields.md)| Register data | [optional] 

### Return type

[**RegistrationRegisterResponse**](RegistrationRegisterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tpay response |  -  |
**403** | Access denied |  -  |
**404** | Invalid api key or password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

