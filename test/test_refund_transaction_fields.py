# coding: utf-8

"""
    Tpay.com Technical Documentation

     <p class=\"changes-disclaimer\"> Demo transaction/masspayments api key: <input type=\"text\" id=\"transaction_key\" value=\"75f86137a6635df826e3efe2e66f7c9a946fdde1\" class=\"ui-form-control\"/><label for=\"transaction_key\" style=\"display: none;\" id=\"tr_api_label\">COPIED!</label><br/><br/> Demo cards api key: <input type=\"text\" id=\"cards_key\" value=\"ba9a05faa697f9b43f39b84933ff168e373c6496\" class=\"ui-form-control\"/><label for=\"cards_key\" style=\"display: none;\" id=\"cards_api_label\">COPIED!</label><br/><br/> Demo registration api key: <input type=\"text\" id=\"registration_key\" value=\"6c0f5ef6e4d6877abad7fcfb3b5de117ad8b772d\" class=\"ui-form-control\"/><label for=\"registration_key\" style=\"display: none;\" id=\"registration_api_label\">COPIED!</label><br/><br/> The terms seller and merchant are used interchangeably and they both refer to a person or a company registered at tpay.com to accept online payments. <br/> Whenever term merchant panel is used it refers to the part of tpay.com website located at <a href=\"https://secure.tpay.com/panel\" target=\"_blank\">secure.tpay.com/panel</a>. <br/><br/> For sandbox purposes use merchant demo account <br/><br/> ID - 1010, Password - demo<br/><br/>Remember that this is a shared account, so all data passed through will be publicly visible.</p>  # noqa: E501

    The version of the OpenAPI document: 1.1.2
    Contact: pt@tpay.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.models.refund_transaction_fields import RefundTransactionFields  # noqa: E501
from openapi_client.rest import ApiException


class TestRefundTransactionFields(unittest.TestCase):
    """RefundTransactionFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRefundTransactionFields(self):
        """Test RefundTransactionFields"""
        # FIXME: construct object with mandatory attributes with example values
        # model = openapi_client.models.refund_transaction_fields.RefundTransactionFields()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
