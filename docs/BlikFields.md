# BlikFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Transaction title | 
**code** | **str** | 6 digit code generated in customer bank mobile app (required if customer does not have registered alias or when customer does not want to pay by regietered device). BLIK code contains only digits but can start with zero or multiple zeroes, so you must not cast this variable to int. | [optional] 
**api_password** | **str** | API password. | 
**alias** | [**list[BlikAlias]**](BlikAlias.md) | Mandatory field when creating oneClick transactions, optional for standart Blik transactions with 6 digit code. In case of alias registration attempt you can send only 1 alias per 1 request. | [optional] 
**type** | **int** | Transaction type. 0 - WEB mode (default value). 1 - POS mode dedicated for payment terminals | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


