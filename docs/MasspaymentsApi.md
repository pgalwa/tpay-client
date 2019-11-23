# openapi_client.MasspaymentsApi

All URIs are relative to *https://secure.tpay.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_gw_api_key_masspayment_authorize_post**](MasspaymentsApi.md#api_gw_api_key_masspayment_authorize_post) | **POST** /api/gw/{api_key}/masspayment/authorize | authorize
[**api_gw_api_key_masspayment_create_post**](MasspaymentsApi.md#api_gw_api_key_masspayment_create_post) | **POST** /api/gw/{api_key}/masspayment/create | create
[**api_gw_api_key_masspayment_packs_post**](MasspaymentsApi.md#api_gw_api_key_masspayment_packs_post) | **POST** /api/gw/{api_key}/masspayment/packs | packs
[**api_gw_api_key_masspayment_transfers_post**](MasspaymentsApi.md#api_gw_api_key_masspayment_transfers_post) | **POST** /api/gw/{api_key}/masspayment/transfers | transfers


# **api_gw_api_key_masspayment_authorize_post**
> MasspaymentAuthorizeResponse api_gw_api_key_masspayment_authorize_post(api_key, basic_data=basic_data)

authorize

This method authorizes the processing of chosen pack of transfers.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.MasspaymentsApi()
api_key = 'api_key_example' # str | The api key.
basic_data = openapi_client.MasspaymentAuthorizeFields() # MasspaymentAuthorizeFields | Transaction data. (optional)

try:
    # authorize
    api_response = api_instance.api_gw_api_key_masspayment_authorize_post(api_key, basic_data=basic_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasspaymentsApi->api_gw_api_key_masspayment_authorize_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. | 
 **basic_data** | [**MasspaymentAuthorizeFields**](MasspaymentAuthorizeFields.md)| Transaction data. | [optional] 

### Return type

[**MasspaymentAuthorizeResponse**](MasspaymentAuthorizeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tpay response |  -  |
**401** | Api password is incorrect |  -  |
**404** | Invalid api key or password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_gw_api_key_masspayment_create_post**
> MasspaymentCreateResponse api_gw_api_key_masspayment_create_post(api_key, basic_data=basic_data)

create

This method adds a pack of transfers to the Tpay system. After executing a correct operation, you need to request authorize method to confirm payout processing. Transfers are being made once a day on workdays. You can find confirmation code in Merchant Panel, settings tab-> notifications. Variable $seller_id is Merchant’s ID in tpay.com system. <br/><br/> <b>Example CSV file</b><br/> Each line contains one transfer formatted as in the example below. Columns are separated by a semicolon. <br/> The file does not have a header.<br/><br/> account number (26 digits);receiver (part 1) (35 characters);receiver (part 2) (35 characters);receiver (part 3) (35 characters);receiver (part 4) (35 characters);amount (dot or comma separator);title (part 1) (35 characters);title (part 2) (35 characters);Tpay transaction ID<br/><br/> Place transfer receiver name in 1-4 receiver fields. Each field can be maximum 35 characters long.<br/> If receiver name is for example 40 characters long, you should put 35 in receiver 1 field, and 5 characters in receiver 2 field.<br/> The same rule is valid for title field. The transaction ID field is not required, whithout this field, the file format looks like this: <br/><br/> account number (26 digits);receiver (part 1) (35 characters);receiver (part 2) (35 characters);receiver (part 3) (35 characters);receiver (part 4) (35 characters);amount (dot or comma separator);title (part 1) (35 characters);title (part 2) (35 characters);Transaction ID from merchant system<br/><br/> Example CSV file can be downloaded from:<br/> <a href=\"https://secure.tpay.com/partner/pliki/przyklad.csv\" target=\"_blank\">Download</a> 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.MasspaymentsApi()
api_key = 'api_key_example' # str | The api key.
basic_data = openapi_client.MasspaymentCreateFields() # MasspaymentCreateFields | Transaction data. (optional)

try:
    # create
    api_response = api_instance.api_gw_api_key_masspayment_create_post(api_key, basic_data=basic_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasspaymentsApi->api_gw_api_key_masspayment_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. | 
 **basic_data** | [**MasspaymentCreateFields**](MasspaymentCreateFields.md)| Transaction data. | [optional] 

### Return type

[**MasspaymentCreateResponse**](MasspaymentCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tpay response |  -  |
**401** | Api password is incorrect |  -  |
**404** | Invalid api key or password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_gw_api_key_masspayment_packs_post**
> MasspaymentPacksResponse api_gw_api_key_masspayment_packs_post(api_key, basic_data=basic_data)

packs

This method allows browsing through created packages. If none of the parameters has been sent, all packages for the Merchant’s account will be returned. If any records exist, there will be pack objects in pack section representing respective transfer packages. You can send pack_id to browse contents of specific pack or send time range to browse all packages within time range

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.MasspaymentsApi()
api_key = 'api_key_example' # str | The api key.
basic_data = openapi_client.MasspaymentPacksFields() # MasspaymentPacksFields | Transaction data. (optional)

try:
    # packs
    api_response = api_instance.api_gw_api_key_masspayment_packs_post(api_key, basic_data=basic_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasspaymentsApi->api_gw_api_key_masspayment_packs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. | 
 **basic_data** | [**MasspaymentPacksFields**](MasspaymentPacksFields.md)| Transaction data. | [optional] 

### Return type

[**MasspaymentPacksResponse**](MasspaymentPacksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tpay response |  -  |
**401** | Api password is incorrect |  -  |
**404** | Invalid api key or password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_gw_api_key_masspayment_transfers_post**
> MasspaymentTransfersResponse api_gw_api_key_masspayment_transfers_post(api_key, basic_data=basic_data)

transfers

This method allows browsing through transfers within one package. Required parameters (besides those described in mass payments main description), at least 1 is obligatory. If any records exist, there will be transfer objects in transfers section representing several transfers.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.MasspaymentsApi()
api_key = 'api_key_example' # str | The api key.
basic_data = openapi_client.MasspaymentTransfersFields() # MasspaymentTransfersFields | Transaction data. (optional)

try:
    # transfers
    api_response = api_instance.api_gw_api_key_masspayment_transfers_post(api_key, basic_data=basic_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MasspaymentsApi->api_gw_api_key_masspayment_transfers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. | 
 **basic_data** | [**MasspaymentTransfersFields**](MasspaymentTransfersFields.md)| Transaction data. | [optional] 

### Return type

[**MasspaymentTransfersResponse**](MasspaymentTransfersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tpay response |  -  |
**401** | Api password is incorrect |  -  |
**404** | Invalid api key or password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

