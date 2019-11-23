# SecuresaleResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_3ds_url** | **str** |  | [optional] 
**result** | [**Result**](Result.md) |  | [optional] 
**test_mode** | **int** |  | [optional] 
**sale_auth** | **str** | Transaction id in tpay.com system | [optional] 
**cli_auth** | **str** | Client token | [optional] 
**currency** | **int** | transaction currency in ISO numeric format | [optional] [default to 985]
**amount** | **float** | transaction amount casted to float | [optional] 
**date** | **str** | Date of payment | [optional] 
**status** | **str** |  | [optional] 
**reason** | **str** | Acquirer (Elavon / eService) rejection code - see \&quot;Card Payments Rejection Codes\&quot; for more details | [optional] 
**card** | **str** | Card number last 4 digits - for example ****1234 | [optional] 
**sign** | **str** | sign is calculated from cryptographic hash function set in Merchant panel (default SHA-1) hash_alg(test_mode + sale_auth + cli_auth + card + currency + amount + date + status + verification code)  | [optional] 
**err_code** | [**CardsErrCode**](CardsErrCode.md) |  | [optional] 
**err_desc** | **str** | Error code description if an error occurs or not present in response. - see \&quot;Card Payments Rejection Codes\&quot; for more details | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


