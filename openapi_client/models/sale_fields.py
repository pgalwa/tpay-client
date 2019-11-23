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


class SaleFields(object):
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
        'cli_auth': 'str',
        'sale_auth': 'str',
        'api_password': 'str',
        'sign': 'str'
    }

    attribute_map = {
        'cli_auth': 'cli_auth',
        'sale_auth': 'sale_auth',
        'api_password': 'api_password',
        'sign': 'sign'
    }

    def __init__(self, cli_auth=None, sale_auth=None, api_password=None, sign=None, local_vars_configuration=None):  # noqa: E501
        """SaleFields - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cli_auth = None
        self._sale_auth = None
        self._api_password = None
        self._sign = None
        self.discriminator = None

        self.cli_auth = cli_auth
        self.sale_auth = sale_auth
        self.api_password = api_password
        self.sign = sign

    @property
    def cli_auth(self):
        """Gets the cli_auth of this SaleFields.  # noqa: E501

        Client token  # noqa: E501

        :return: The cli_auth of this SaleFields.  # noqa: E501
        :rtype: str
        """
        return self._cli_auth

    @cli_auth.setter
    def cli_auth(self, cli_auth):
        """Sets the cli_auth of this SaleFields.

        Client token  # noqa: E501

        :param cli_auth: The cli_auth of this SaleFields.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cli_auth is None:  # noqa: E501
            raise ValueError("Invalid value for `cli_auth`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cli_auth is not None and len(cli_auth) > 40):
            raise ValueError("Invalid value for `cli_auth`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cli_auth is not None and len(cli_auth) < 40):
            raise ValueError("Invalid value for `cli_auth`, length must be greater than or equal to `40`")  # noqa: E501

        self._cli_auth = cli_auth

    @property
    def sale_auth(self):
        """Gets the sale_auth of this SaleFields.  # noqa: E501

        Transaction id in tpay.com system  # noqa: E501

        :return: The sale_auth of this SaleFields.  # noqa: E501
        :rtype: str
        """
        return self._sale_auth

    @sale_auth.setter
    def sale_auth(self, sale_auth):
        """Sets the sale_auth of this SaleFields.

        Transaction id in tpay.com system  # noqa: E501

        :param sale_auth: The sale_auth of this SaleFields.  # noqa: E501
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
    def api_password(self):
        """Gets the api_password of this SaleFields.  # noqa: E501

        API password.  # noqa: E501

        :return: The api_password of this SaleFields.  # noqa: E501
        :rtype: str
        """
        return self._api_password

    @api_password.setter
    def api_password(self, api_password):
        """Sets the api_password of this SaleFields.

        API password.  # noqa: E501

        :param api_password: The api_password of this SaleFields.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and api_password is None:  # noqa: E501
            raise ValueError("Invalid value for `api_password`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                api_password is not None and len(api_password) > 40):
            raise ValueError("Invalid value for `api_password`, length must be less than or equal to `40`")  # noqa: E501

        self._api_password = api_password

    @property
    def sign(self):
        """Gets the sign of this SaleFields.  # noqa: E501

        Request sign is calculated from cryptographic hash function set in Merchant’s Panel (default SHA-1): hash_alg (method + cli_auth + sale_auth + verification code); where + means concatenation. Passed cli_auth has to match with cli_auth used while creating sale in presale method.   # noqa: E501

        :return: The sign of this SaleFields.  # noqa: E501
        :rtype: str
        """
        return self._sign

    @sign.setter
    def sign(self, sign):
        """Sets the sign of this SaleFields.

        Request sign is calculated from cryptographic hash function set in Merchant’s Panel (default SHA-1): hash_alg (method + cli_auth + sale_auth + verification code); where + means concatenation. Passed cli_auth has to match with cli_auth used while creating sale in presale method.   # noqa: E501

        :param sign: The sign of this SaleFields.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sign is None:  # noqa: E501
            raise ValueError("Invalid value for `sign`, must not be `None`")  # noqa: E501

        self._sign = sign

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
        if not isinstance(other, SaleFields):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SaleFields):
            return True

        return self.to_dict() != other.to_dict()