# PresaleFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desc** | **str** | transaction description | 
**cli_auth** | **str** | Client token | 
**amount** | **float** | transaction amount casted to float | 
**api_password** | **str** | API password. | 
**sign** | **str** | Sign is calculated from cryptographic hash function set in Merchant’s Panel (default SHA-1): hash_alg (method + cli_auth + desc + amount + currency + order_id + language + verification code) where + means concatenation. | 
**currency** | **int** | transaction currency in ISO numeric format | [optional] [default to 985]
**order_id** | **str** | merchant order ID used to recognise payment | [optional] 
**language** | [**Language**](Language.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


