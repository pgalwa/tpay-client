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


class CreateResponse(object):
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
        'err': 'TransactionErrorCodes',
        'title': 'str',
        'amount': 'float',
        'account_number': 'float',
        'online': 'int',
        'url': 'str',
        'desc': 'str'
    }

    attribute_map = {
        'result': 'result',
        'err': 'err',
        'title': 'title',
        'amount': 'amount',
        'account_number': 'account_number',
        'online': 'online',
        'url': 'url',
        'desc': 'desc'
    }

    def __init__(self, result=None, err=None, title=None, amount=None, account_number=None, online=None, url=None, desc=None, local_vars_configuration=None):  # noqa: E501
        """CreateResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._result = None
        self._err = None
        self._title = None
        self._amount = None
        self._account_number = None
        self._online = None
        self._url = None
        self._desc = None
        self.discriminator = None

        self.result = result
        if err is not None:
            self.err = err
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        if account_number is not None:
            self.account_number = account_number
        if online is not None:
            self.online = online
        if url is not None:
            self.url = url
        if desc is not None:
            self.desc = desc

    @property
    def result(self):
        """Gets the result of this CreateResponse.  # noqa: E501


        :return: The result of this CreateResponse.  # noqa: E501
        :rtype: Result
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this CreateResponse.


        :param result: The result of this CreateResponse.  # noqa: E501
        :type: Result
        """
        if self.local_vars_configuration.client_side_validation and result is None:  # noqa: E501
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def err(self):
        """Gets the err of this CreateResponse.  # noqa: E501


        :return: The err of this CreateResponse.  # noqa: E501
        :rtype: TransactionErrorCodes
        """
        return self._err

    @err.setter
    def err(self, err):
        """Sets the err of this CreateResponse.


        :param err: The err of this CreateResponse.  # noqa: E501
        :type: TransactionErrorCodes
        """

        self._err = err

    @property
    def title(self):
        """Gets the title of this CreateResponse.  # noqa: E501

        Transaction title  # noqa: E501

        :return: The title of this CreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreateResponse.

        Transaction title  # noqa: E501

        :param title: The title of this CreateResponse.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def amount(self):
        """Gets the amount of this CreateResponse.  # noqa: E501

        transaction amount casted to float  # noqa: E501

        :return: The amount of this CreateResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreateResponse.

        transaction amount casted to float  # noqa: E501

        :param amount: The amount of this CreateResponse.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                amount is not None and amount < 0.1):  # noqa: E501
            raise ValueError("Invalid value for `amount`, must be a value greater than or equal to `0.1`")  # noqa: E501

        self._amount = amount

    @property
    def account_number(self):
        """Gets the account_number of this CreateResponse.  # noqa: E501

        bank account number (only for manual bank transfers)  # noqa: E501

        :return: The account_number of this CreateResponse.  # noqa: E501
        :rtype: float
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this CreateResponse.

        bank account number (only for manual bank transfers)  # noqa: E501

        :param account_number: The account_number of this CreateResponse.  # noqa: E501
        :type: float
        """

        self._account_number = account_number

    @property
    def online(self):
        """Gets the online of this CreateResponse.  # noqa: E501

        Booking payments online indicator  # noqa: E501

        :return: The online of this CreateResponse.  # noqa: E501
        :rtype: int
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this CreateResponse.

        Booking payments online indicator  # noqa: E501

        :param online: The online of this CreateResponse.  # noqa: E501
        :type: int
        """

        self._online = online

    @property
    def url(self):
        """Gets the url of this CreateResponse.  # noqa: E501

        Link to transaction (for redirecting to payment)  # noqa: E501

        :return: The url of this CreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CreateResponse.

        Link to transaction (for redirecting to payment)  # noqa: E501

        :param url: The url of this CreateResponse.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def desc(self):
        """Gets the desc of this CreateResponse.  # noqa: E501

        optional field, contains names of invalid fields.  # noqa: E501

        :return: The desc of this CreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this CreateResponse.

        optional field, contains names of invalid fields.  # noqa: E501

        :param desc: The desc of this CreateResponse.  # noqa: E501
        :type: str
        """

        self._desc = desc

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
        if not isinstance(other, CreateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateResponse):
            return True

        return self.to_dict() != other.to_dict()
