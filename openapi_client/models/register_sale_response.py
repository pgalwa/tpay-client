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


class RegisterSaleResponse(object):
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
        'sale_auth': 'str',
        'err_code': 'CardsErrCode',
        'err_desc': 'str'
    }

    attribute_map = {
        'result': 'result',
        'sale_auth': 'sale_auth',
        'err_code': 'err_code',
        'err_desc': 'err_desc'
    }

    def __init__(self, result=None, sale_auth=None, err_code=None, err_desc=None, local_vars_configuration=None):  # noqa: E501
        """RegisterSaleResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._result = None
        self._sale_auth = None
        self._err_code = None
        self._err_desc = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if sale_auth is not None:
            self.sale_auth = sale_auth
        if err_code is not None:
            self.err_code = err_code
        if err_desc is not None:
            self.err_desc = err_desc

    @property
    def result(self):
        """Gets the result of this RegisterSaleResponse.  # noqa: E501


        :return: The result of this RegisterSaleResponse.  # noqa: E501
        :rtype: Result
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this RegisterSaleResponse.


        :param result: The result of this RegisterSaleResponse.  # noqa: E501
        :type: Result
        """

        self._result = result

    @property
    def sale_auth(self):
        """Gets the sale_auth of this RegisterSaleResponse.  # noqa: E501

        Transaction id in tpay.com system  # noqa: E501

        :return: The sale_auth of this RegisterSaleResponse.  # noqa: E501
        :rtype: str
        """
        return self._sale_auth

    @sale_auth.setter
    def sale_auth(self, sale_auth):
        """Sets the sale_auth of this RegisterSaleResponse.

        Transaction id in tpay.com system  # noqa: E501

        :param sale_auth: The sale_auth of this RegisterSaleResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                sale_auth is not None and len(sale_auth) > 40):
            raise ValueError("Invalid value for `sale_auth`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sale_auth is not None and len(sale_auth) < 40):
            raise ValueError("Invalid value for `sale_auth`, length must be greater than or equal to `40`")  # noqa: E501

        self._sale_auth = sale_auth

    @property
    def err_code(self):
        """Gets the err_code of this RegisterSaleResponse.  # noqa: E501


        :return: The err_code of this RegisterSaleResponse.  # noqa: E501
        :rtype: CardsErrCode
        """
        return self._err_code

    @err_code.setter
    def err_code(self, err_code):
        """Sets the err_code of this RegisterSaleResponse.


        :param err_code: The err_code of this RegisterSaleResponse.  # noqa: E501
        :type: CardsErrCode
        """

        self._err_code = err_code

    @property
    def err_desc(self):
        """Gets the err_desc of this RegisterSaleResponse.  # noqa: E501

        Error code description if an error occurs or not present in response. - see \"Card Payments Rejection Codes\" for more details  # noqa: E501

        :return: The err_desc of this RegisterSaleResponse.  # noqa: E501
        :rtype: str
        """
        return self._err_desc

    @err_desc.setter
    def err_desc(self, err_desc):
        """Sets the err_desc of this RegisterSaleResponse.

        Error code description if an error occurs or not present in response. - see \"Card Payments Rejection Codes\" for more details  # noqa: E501

        :param err_desc: The err_desc of this RegisterSaleResponse.  # noqa: E501
        :type: str
        """

        self._err_desc = err_desc

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
        if not isinstance(other, RegisterSaleResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegisterSaleResponse):
            return True

        return self.to_dict() != other.to_dict()