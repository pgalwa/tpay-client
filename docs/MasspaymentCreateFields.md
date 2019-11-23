# MasspaymentCreateFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csv** | **str** | Transfers list encoded with base64. Format has been described in metchod description | 
**api_password** | **str** | API password. | 
**sign** | **str** | Checksum to verify parameters received from Merchant. Generated according to outline below using SHA1 function: SHA1(seller_id + transfers list (before encrypting in base64) + Merchant confirmation code) Implementing checksum in PHP: sha1($seller_id. $csv . $confirmation_code)  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


