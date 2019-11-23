# DeregisterFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cli_auth** | **str** | Client token | 
**language** | [**Language**](Language.md) |  | [optional] 
**api_password** | **str** | API password. | 
**sign** | **str** | Sign is calculated from cryptographic hash function set in Merchant’s Panel (default SHA-1): hash_alg (method + cli_auth + language + verification code) where + means concatenation. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


