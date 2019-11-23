# RegisterFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Merchant email. Access data for Tpay.com account will be send on this email after registration. | 
**name** | **str** | Merchant&#39;s company name. | 
**nip** | **str** | Taxpayer identification number. | 
**regon** | **str** | National Business Registry Number. | [optional] 
**krsedg** | **str** | Entry number from National Court Register | [optional] 
**legal_form** | **str** | Legal Form Id received from &#39;inputs&#39; method. | 
**branche** | **int** | Branche id received from &#39;inputs&#39; method. | 
**website** | **str** | Merchant&#39;s website | [optional] 
**phone** | **str** | Merchant phone number | 
**address_street** | **str** | Merchant&#39;s company street address. | 
**address_block** | **str** | Merchant&#39;s company block number. | 
**address_nr** | **str** | Merchant&#39;s company local number. | 
**address_city** | **str** | Merchant&#39;s company city address. | 
**address_code** | **str** | Merchant&#39;s company city postal code. | 
**create_api** | **int** | Generate access for API transaction. Access data (api_key and  api_password) will be returned in response. | [optional] 
**offer_code** | **str** | Offer code dedicate for merchant and  generate by Sales Department. | [optional] 
**test** | **int** | Parameter allows recieved an example response with merchant data without creating new account in Tpay.com system. Parameter is obligatory in initial stage of integration. | [optional] 
**api_password** | **str** | API password. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


