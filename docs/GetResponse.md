# GetResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Result**](Result.md) |  | [optional] 
**status** | **str** |  | [optional] 
**error_code** | **str** | Depending on setting in merchant panel, error_code may be different than none for correct status, when acceptance of overpays and surcharges has been set. | [optional] 
**start_time** | **str** | Transaction creation time | [optional] 
**payment_time** | **str** | Date of payment or empty for pending transactions | [optional] 
**chargeback_time** | **str** | Date of payment refund or empty for not refunded transactions | [optional] 
**channel** | **int** | Payment channel ID can be recognised in merchant panel (your offer section) | [optional] 
**test_mode** | **int** | Returns 1 if transaction was in test mode | [optional] 
**amount** | **float** | transaction amount casted to float | [optional] 
**amount_paid** | **float** | The amount paid by customer | [optional] 
**name** | **str** | customer name | [optional] 
**email** | **str** | customer email | [optional] 
**address** | **str** | customer address (parameter is empty if this field was not send with create method) | [optional] 
**code** | **str** | customer postal code (parameter is empty if this field was not send with create method) | [optional] 
**city** | **str** | customer city (parameter is empty if this field was not send with create method) | [optional] 
**phone** | **str** | customer phone number (parameter is empty if this field was not send with create method) | [optional] 
**country** | **str** | Two letters - see ISO 3166-1 document | [optional] 
**err** | [**TransactionErrorCodes**](TransactionErrorCodes.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


