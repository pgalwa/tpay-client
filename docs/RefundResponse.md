# RefundResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Result**](Result.md) |  | 
**test_mode** | **int** |  | [optional] 
**sale_auth** | **str** | Transaction id in tpay.com system | 
**sale_ref** | **str** |  | [optional] 
**currency** | **int** | transaction currency in ISO numeric format | [default to 985]
**amount** | **float** | transaction amount casted to float | 
**date** | **str** | Date of payment | [optional] 
**status** | **str** |  | 
**reason** | **str** | Acquirer (Elavon / eService) rejection code - see \&quot;Card Payments Rejection Codes\&quot; for more details | [optional] 
**sign** | **str** | Response sign &#x3D; hash_alg(test_mode + sale_auth + sale_ref + order_id + cli_auth + card + currency + amount + date + status + reason + verification code).  | 
**card** | **str** |  | [optional] 
**cli_auth** | **str** | Client token | [optional] 
**err_code** | [**CardsErrCode**](CardsErrCode.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


