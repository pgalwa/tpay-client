# SaleResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Result**](Result.md) |  | 
**test_mode** | **int** |  | [optional] 
**sale_auth** | **str** | Transaction id in tpay.com system | 
**cli_auth** | **str** | Client token | [optional] 
**currency** | **int** | transaction currency in ISO numeric format | [default to 985]
**amount** | **float** | transaction amount casted to float | 
**date** | **str** | Date of payment | [optional] 
**status** | **str** |  | 
**reason** | **str** | Acquirer (Elavon / eService) rejection code - see \&quot;Card Payments Rejection Codes\&quot; for more details | [optional] 
**sign** | **str** | Response sign &#x3D; hash_alg(sale_auth + cli_auth + currency + amount + sale_date+ status + reason + verification code) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


