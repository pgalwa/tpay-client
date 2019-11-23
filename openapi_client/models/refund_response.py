# coding: utf-8

"""
    Tpay.com Technical Documentation

     <p class=\"changes-disclaimer\"> Demo transaction/masspayments api key: <input type=\"text\" id=\"transaction_key\" value=\"75f86137a6635df826e3efe2e66f7c9a946fdde1\" class=\"ui-form-control\"/><label for=\"transaction_key\" style=\"display: none;\" id=\"tr_api_label\">COPIED!</label><br/><br/> Demo cards api key: <input type=\"text\" id=\"cards_key\" value=\"ba9a05faa697f9b43f39b84933ff168e373c6496\" class=\"ui-form-control\"/><label for=\"cards_key\" style=\"display: none;\" id=\"cards_api_label\">COPIED!</label><br/><br/> Demo registration api key: <input type=\"text\" id=\"registration_key\" value=\"6c0f5ef6e4d6877abad7fcfb3b5de117ad8b772d\" class=\"ui-form-control\"/><label for=\"registration_key\" style=\"display: none;\" id=\"registration_api_label\">COPIED!</label><br/><br/> The terms seller and merchant are used interchangeably and they both refer to a person or a company registered at tpay.com to accept online payments. <br/> Whenever term merchant panel is used it refers to the part of tpay.com website located at <a href=\"https://secure.tpay.com/panel\" target=\"_blank\">secure.tpay.com/panel</a>. <br/><br/> For sandbox purposes use merchant demo account <br/><br/> ID - 1010, Password - demo<br/><br/>Remember that this is a shared account, so all data passed through will be publicly visible.</p>  # noqa: E501

    The version of the OpenAPI document: 1.1.2
    Contact: pt@tpay.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class RefundResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'result': 'Result',
        'test_mode': 'int',
        'sale_auth': 'str',
        'sale_ref': 'str',
        'currency': 'int',
        'amount': 'float',
        'date': 'str',
        'status': 'str',
        'reason': 'str',
        'sign': 'str',
        'card': 'str',
        'cli_auth': 'str',
        'err_code': 'CardsErrCode'
    }

    attribute_map = {
        'result': 'result',
        'test_mode': 'test_mode',
        'sale_auth': 'sale_auth',
        'sale_ref': 'sale_ref',
        'currency': 'currency',
        'amount': 'amount',
        'date': 'date',
        'status': 'status',
        'reason': 'reason',
        'sign': 'sign',
        'card': 'card',
        'cli_auth': 'cli_auth',
        'err_code': 'err_code'
    }

    def __init__(self, result=None, test_mode=None, sale_auth=None, sale_ref=None, currency=985, amount=None, date=None, status=None, reason=None, sign=None, card=None, cli_auth=None, err_code=None, local_vars_configuration=None):  # noqa: E501
        """RefundResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._result = None
        self._test_mode = None
        self._sale_auth = None
        self._sale_ref = None
        self._currency = None
        self._amount = None
        self._date = None
        self._status = None
        self._reason = None
        self._sign = None
        self._card = None
        self._cli_auth = None
        self._err_code = None
        self.discriminator = None

        self.result = result
        if test_mode is not None:
            self.test_mode = test_mode
        self.sale_auth = sale_auth
        if sale_ref is not None:
            self.sale_ref = sale_ref
        self.currency = currency
        self.amount = amount
        if date is not None:
            self.date = date
        self.status = status
        if reason is not None:
            self.reason = reason
        self.sign = sign
        if card is not None:
            self.card = card
        if cli_auth is not None:
            self.cli_auth = cli_auth
        if err_code is not None:
            self.err_code = err_code

    @property
    def result(self):
        """Gets the result of this RefundResponse.  # noqa: E501


        :return: The result of this RefundResponse.  # noqa: E501
        :rtype: Result
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this RefundResponse.


        :param result: The result of this RefundResponse.  # noqa: E501
        :type: Result
        """
        if self.local_vars_configuration.client_side_validation and result is None:  # noqa: E501
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def test_mode(self):
        """Gets the test_mode of this RefundResponse.  # noqa: E501


        :return: The test_mode of this RefundResponse.  # noqa: E501
        :rtype: int
        """
        return self._test_mode

    @test_mode.setter
    def test_mode(self, test_mode):
        """Sets the test_mode of this RefundResponse.


        :param test_mode: The test_mode of this RefundResponse.  # noqa: E501
        :type: int
        """

        self._test_mode = test_mode

    @property
    def sale_auth(self):
        """Gets the sale_auth of this RefundResponse.  # noqa: E501

        Transaction id in tpay.com system  # noqa: E501

        :return: The sale_auth of this RefundResponse.  # noqa: E501
        :rtype: str
        """
        return self._sale_auth

    @sale_auth.setter
    def sale_auth(self, sale_auth):
        """Sets the sale_auth of this RefundResponse.

        Transaction id in tpay.com system  # noqa: E501

        :param sale_auth: The sale_auth of this RefundResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sale_auth is None:  # noqa: E501
            raise ValueError("Invalid value for `sale_auth`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sale_auth is not None and len(sale_auth) > 40):
            raise ValueError("Invalid value for `sale_auth`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sale_auth is not None and len(sale_auth) < 40):
            raise ValueError("Invalid value for `sale_auth`, length must be greater than or equal to `40`")  # noqa: E501

        self._sale_auth = sale_auth

    @property
    def sale_ref(self):
        """Gets the sale_ref of this RefundResponse.  # noqa: E501


        :return: The sale_ref of this RefundResponse.  # noqa: E501
        :rtype: str
        """
        return self._sale_ref

    @sale_ref.setter
    def sale_ref(self, sale_ref):
        """Sets the sale_ref of this RefundResponse.


        :param sale_ref: The sale_ref of this RefundResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                sale_ref is not None and len(sale_ref) > 40):
            raise ValueError("Invalid value for `sale_ref`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sale_ref is not None and len(sale_ref) < 40):
            raise ValueError("Invalid value for `sale_ref`, length must be greater than or equal to `40`")  # noqa: E501

        self._sale_ref = sale_ref

    @property
    def currency(self):
        """Gets the currency of this RefundResponse.  # noqa: E501

        transaction currency in ISO numeric format  # noqa: E501

        :return: The currency of this RefundResponse.  # noqa: E501
        :rtype: int
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this RefundResponse.

        transaction currency in ISO numeric format  # noqa: E501

        :param currency: The currency of this RefundResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def amount(self):
        """Gets the amount of this RefundResponse.  # noqa: E501

        transaction amount casted to float  # noqa: E501

        :return: The amount of this RefundResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this RefundResponse.

        transaction amount casted to float  # noqa: E501

        :param amount: The amount of this RefundResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                amount is not None and amount < 0.1):  # noqa: E501
            raise ValueError("Invalid value for `amount`, must be a value greater than or equal to `0.1`")  # noqa: E501

        self._amount = amount

    @property
    def date(self):
        """Gets the date of this RefundResponse.  # noqa: E501

        Date of payment  # noqa: E501

        :return: The date of this RefundResponse.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this RefundResponse.

        Date of payment  # noqa: E501

        :param date: The date of this RefundResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                date is not None and not re.search(r'YYYY-MM-DD HH:mm:ss', date)):  # noqa: E501
            raise ValueError(r"Invalid value for `date`, must be a follow pattern or equal to `/YYYY-MM-DD HH:mm:ss/`")  # noqa: E501

        self._date = date

    @property
    def status(self):
        """Gets the status of this RefundResponse.  # noqa: E501


        :return: The status of this RefundResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RefundResponse.


        :param status: The status of this RefundResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["correct", "declined"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def reason(self):
        """Gets the reason of this RefundResponse.  # noqa: E501

        Acquirer (Elavon / eService) rejection code - see \"Card Payments Rejection Codes\" for more details  # noqa: E501

        :return: The reason of this RefundResponse.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this RefundResponse.

        Acquirer (Elavon / eService) rejection code - see \"Card Payments Rejection Codes\" for more details  # noqa: E501

        :param reason: The reason of this RefundResponse.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def sign(self):
        """Gets the sign of this RefundResponse.  # noqa: E501

        Response sign = hash_alg(test_mode + sale_auth + sale_ref + order_id + cli_auth + card + currency + amount + date + status + reason + verification code).   # noqa: E501

        :return: The sign of this RefundResponse.  # noqa: E501
        :rtype: str
        """
        return self._sign

    @sign.setter
    def sign(self, sign):
        """Sets the sign of this RefundResponse.

        Response sign = hash_alg(test_mode + sale_auth + sale_ref + order_id + cli_auth + card + currency + amount + date + status + reason + verification code).   # noqa: E501

        :param sign: The sign of this RefundResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sign is None:  # noqa: E501
            raise ValueError("Invalid value for `sign`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sign is not None and len(sign) > 128):
            raise ValueError("Invalid value for `sign`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sign is not None and len(sign) < 40):
            raise ValueError("Invalid value for `sign`, length must be greater than or equal to `40`")  # noqa: E501

        self._sign = sign

    @property
    def card(self):
        """Gets the card of this RefundResponse.  # noqa: E501


        :return: The card of this RefundResponse.  # noqa: E501
        :rtype: str
        """
        return self._card

    @card.setter
    def card(self, card):
        """Sets the card of this RefundResponse.


        :param card: The card of this RefundResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                card is not None and len(card) > 8):
            raise ValueError("Invalid value for `card`, length must be less than or equal to `8`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                card is not None and len(card) < 8):
            raise ValueError("Invalid value for `card`, length must be greater than or equal to `8`")  # noqa: E501

        self._card = card

    @property
    def cli_auth(self):
        """Gets the cli_auth of this RefundResponse.  # noqa: E501

        Client token  # noqa: E501

        :return: The cli_auth of this RefundResponse.  # noqa: E501
        :rtype: str
        """
        return self._cli_auth

    @cli_auth.setter
    def cli_auth(self, cli_auth):
        """Sets the cli_auth of this RefundResponse.

        Client token  # noqa: E501

        :param cli_auth: The cli_auth of this RefundResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                cli_auth is not None and len(cli_auth) > 40):
            raise ValueError("Invalid value for `cli_auth`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cli_auth is not None and len(cli_auth) < 40):
            raise ValueError("Invalid value for `cli_auth`, length must be greater than or equal to `40`")  # noqa: E501

        self._cli_auth = cli_auth

    @property
    def err_code(self):
        """Gets the err_code of this RefundResponse.  # noqa: E501


        :return: The err_code of this RefundResponse.  # noqa: E501
        :rtype: CardsErrCode
        """
        return self._err_code

    @err_code.setter
    def err_code(self, err_code):
        """Sets the err_code of this RefundResponse.


        :param err_code: The err_code of this RefundResponse.  # noqa: E501
        :type: CardsErrCode
        """

        self._err_code = err_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RefundResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RefundResponse):
            return True

        return self.to_dict() != other.to_dict()