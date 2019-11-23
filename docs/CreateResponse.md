# CreateResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Result**](Result.md) |  | 
**err** | [**TransactionErrorCodes**](TransactionErrorCodes.md) |  | [optional] 
**title** | **str** | Transaction title | [optional] 
**amount** | **float** | transaction amount casted to float | [optional] 
**account_number** | **float** | bank account number (only for manual bank transfers) | [optional] 
**online** | **int** | Booking payments online indicator | [optional] 
**url** | **str** | Link to transaction (for redirecting to payment) | [optional] 
**desc** | **str** | optional field, contains names of invalid fields. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


