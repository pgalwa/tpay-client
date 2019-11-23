# SaleFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cli_auth** | **str** | Client token | 
**sale_auth** | **str** | Transaction id in tpay.com system | 
**api_password** | **str** | API password. | 
**sign** | **str** | Request sign is calculated from cryptographic hash function set in Merchant’s Panel (default SHA-1): hash_alg (method + cli_auth + sale_auth + verification code); where + means concatenation. Passed cli_auth has to match with cli_auth used while creating sale in presale method.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


