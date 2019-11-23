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


class BlikFields(object):
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
        'title': 'str',
        'code': 'str',
        'api_password': 'str',
        'alias': 'list[BlikAlias]',
        'type': 'int'
    }

    attribute_map = {
        'title': 'title',
        'code': 'code',
        'api_password': 'api_password',
        'alias': 'alias',
        'type': 'type'
    }

    def __init__(self, title=None, code=None, api_password=None, alias=None, type=None, local_vars_configuration=None):  # noqa: E501
        """BlikFields - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._code = None
        self._api_password = None
        self._alias = None
        self._type = None
        self.discriminator = None

        self.title = title
        if code is not None:
            self.code = code
        self.api_password = api_password
        if alias is not None:
            self.alias = alias
        if type is not None:
            self.type = type

    @property
    def title(self):
        """Gets the title of this BlikFields.  # noqa: E501

        Transaction title  # noqa: E501

        :return: The title of this BlikFields.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this BlikFields.

        Transaction title  # noqa: E501

        :param title: The title of this BlikFields.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def code(self):
        """Gets the code of this BlikFields.  # noqa: E501

        6 digit code generated in customer bank mobile app (required if customer does not have registered alias or when customer does not want to pay by regietered device). BLIK code contains only digits but can start with zero or multiple zeroes, so you must not cast this variable to int.  # noqa: E501

        :return: The code of this BlikFields.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this BlikFields.

        6 digit code generated in customer bank mobile app (required if customer does not have registered alias or when customer does not want to pay by regietered device). BLIK code contains only digits but can start with zero or multiple zeroes, so you must not cast this variable to int.  # noqa: E501

        :param code: The code of this BlikFields.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 6):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `6`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) < 6):
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `6`")  # noqa: E501

        self._code = code

    @property
    def api_password(self):
        """Gets the api_password of this BlikFields.  # noqa: E501

        API password.  # noqa: E501

        :return: The api_password of this BlikFields.  # noqa: E501
        :rtype: str
        """
        return self._api_password

    @api_password.setter
    def api_password(self, api_password):
        """Sets the api_password of this BlikFields.

        API password.  # noqa: E501

        :param api_password: The api_password of this BlikFields.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and api_password is None:  # noqa: E501
            raise ValueError("Invalid value for `api_password`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                api_password is not None and len(api_password) > 40):
            raise ValueError("Invalid value for `api_password`, length must be less than or equal to `40`")  # noqa: E501

        self._api_password = api_password

    @property
    def alias(self):
        """Gets the alias of this BlikFields.  # noqa: E501

        Mandatory field when creating oneClick transactions, optional for standart Blik transactions with 6 digit code. In case of alias registration attempt you can send only 1 alias per 1 request.  # noqa: E501

        :return: The alias of this BlikFields.  # noqa: E501
        :rtype: list[BlikAlias]
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this BlikFields.

        Mandatory field when creating oneClick transactions, optional for standart Blik transactions with 6 digit code. In case of alias registration attempt you can send only 1 alias per 1 request.  # noqa: E501

        :param alias: The alias of this BlikFields.  # noqa: E501
        :type: list[BlikAlias]
        """

        self._alias = alias

    @property
    def type(self):
        """Gets the type of this BlikFields.  # noqa: E501

        Transaction type. 0 - WEB mode (default value). 1 - POS mode dedicated for payment terminals  # noqa: E501

        :return: The type of this BlikFields.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BlikFields.

        Transaction type. 0 - WEB mode (default value). 1 - POS mode dedicated for payment terminals  # noqa: E501

        :param type: The type of this BlikFields.  # noqa: E501
        :type: int
        """

        self._type = type

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
        if not isinstance(other, BlikFields):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BlikFields):
            return True

        return self.to_dict() != other.to_dict()
