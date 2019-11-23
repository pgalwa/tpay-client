# SecuresaleFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | customer name | 
**email** | **str** | customer email | 
**desc** | **str** | transaction description | 
**amount** | **float** | transaction amount casted to float | 
**api_password** | **str** | API password. | 
**sign** | **str** | Sign is calculated from cryptographic hash function set in Merchant panel (default SHA-1) hash_alg (method + card + name + email + desc + amount + currency + order_id + onetimer + language + enable_pow_url + verification code) where + means concatenation.  | 
**currency** | **int** | transaction currency in ISO numeric format | [default to 985]
**onetimer** | [**Onetimer**](Onetimer.md) |  | [optional] 
**pow_url** | **str** | url to redirect customer in case of payment success | [optional] 
**pow_url_blad** | **str** | url to redirect customer in case of payment failure | [optional] 
**order_id** | **str** | merchant order ID used to recognise payment | [optional] 
**language** | [**Language**](Language.md) |  | [optional] 
**enable_pow_url** | **int** |  | [optional] 
**card** | **str** | Card hash calculated by schema described in method description | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


