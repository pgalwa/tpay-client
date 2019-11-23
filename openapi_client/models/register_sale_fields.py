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


class RegisterSaleFields(object):
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
        'name': 'str',
        'email': 'str',
        'desc': 'str',
        'amount': 'float',
        'api_password': 'str',
        'sign': 'str',
        'currency': 'int',
        'onetimer': 'Onetimer',
        'pow_url': 'str',
        'pow_url_blad': 'str',
        'order_id': 'str',
        'language': 'Language'
    }

    attribute_map = {
        'name': 'name',
        'email': 'email',
        'desc': 'desc',
        'amount': 'amount',
        'api_password': 'api_password',
        'sign': 'sign',
        'currency': 'currency',
        'onetimer': 'onetimer',
        'pow_url': 'pow_url',
        'pow_url_blad': 'pow_url_blad',
        'order_id': 'order_id',
        'language': 'language'
    }

    def __init__(self, name=None, email=None, desc=None, amount=None, api_password=None, sign=None, currency=985, onetimer=None, pow_url=None, pow_url_blad=None, order_id=None, language=None, local_vars_configuration=None):  # noqa: E501
        """RegisterSaleFields - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._email = None
        self._desc = None
        self._amount = None
        self._api_password = None
        self._sign = None
        self._currency = None
        self._onetimer = None
        self._pow_url = None
        self._pow_url_blad = None
        self._order_id = None
        self._language = None
        self.discriminator = None

        self.name = name
        self.email = email
        self.desc = desc
        self.amount = amount
        self.api_password = api_password
        self.sign = sign
        if currency is not None:
            self.currency = currency
        if onetimer is not None:
            self.onetimer = onetimer
        if pow_url is not None:
            self.pow_url = pow_url
        if pow_url_blad is not None:
            self.pow_url_blad = pow_url_blad
        if order_id is not None:
            self.order_id = order_id
        if language is not None:
            self.language = language

    @property
    def name(self):
        """Gets the name of this RegisterSaleFields.  # noqa: E501

        customer name  # noqa: E501

        :return: The name of this RegisterSaleFields.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RegisterSaleFields.

        customer name  # noqa: E501

        :param name: The name of this RegisterSaleFields.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 64):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501

        self._name = name

    @property
    def email(self):
        """Gets the email of this RegisterSaleFields.  # noqa: E501

        customer email  # noqa: E501

        :return: The email of this RegisterSaleFields.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this RegisterSaleFields.

        customer email  # noqa: E501

        :param email: The email of this RegisterSaleFields.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 64):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `64`")  # noqa: E501

        self._email = email

    @property
    def desc(self):
        """Gets the desc of this RegisterSaleFields.  # noqa: E501

        transaction description  # noqa: E501

        :return: The desc of this RegisterSaleFields.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this RegisterSaleFields.

        transaction description  # noqa: E501

        :param desc: The desc of this RegisterSaleFields.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and desc is None:  # noqa: E501
            raise ValueError("Invalid value for `desc`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                desc is not None and len(desc) > 128):
            raise ValueError("Invalid value for `desc`, length must be less than or equal to `128`")  # noqa: E501

        self._desc = desc

    @property
    def amount(self):
        """Gets the amount of this RegisterSaleFields.  # noqa: E501

        transaction amount casted to float  # noqa: E501

        :return: The amount of this RegisterSaleFields.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this RegisterSaleFields.

        transaction amount casted to float  # noqa: E501

        :param amount: The amount of this RegisterSaleFields.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                amount is not None and amount < 0.1):  # noqa: E501
            raise ValueError("Invalid value for `amount`, must be a value greater than or equal to `0.1`")  # noqa: E501

        self._amount = amount

    @property
    def api_password(self):
        """Gets the api_password of this RegisterSaleFields.  # noqa: E501

        API password.  # noqa: E501

        :return: The api_password of this RegisterSaleFields.  # noqa: E501
        :rtype: str
        """
        return self._api_password

    @api_password.setter
    def api_password(self, api_password):
        """Sets the api_password of this RegisterSaleFields.

        API password.  # noqa: E501

        :param api_password: The api_password of this RegisterSaleFields.  # noqa: E501
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
        """Gets the sign of this RegisterSaleFields.  # noqa: E501

        Sign is calculated from cryptographic hash function set in Merchant’s Panel (default SHA-1): sha1(method + name + email + desc + amount + currency + order_id + onetimer + language + verification code) where + means concatenation.  # noqa: E501

        :return: The sign of this RegisterSaleFields.  # noqa: E501
        :rtype: str
        """
        return self._sign

    @sign.setter
    def sign(self, sign):
        """Sets the sign of this RegisterSaleFields.

        Sign is calculated from cryptographic hash function set in Merchant’s Panel (default SHA-1): sha1(method + name + email + desc + amount + currency + order_id + onetimer + language + verification code) where + means concatenation.  # noqa: E501

        :param sign: The sign of this RegisterSaleFields.  # noqa: E501
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
    def currency(self):
        """Gets the currency of this RegisterSaleFields.  # noqa: E501

        transaction currency in ISO numeric format  # noqa: E501

        :return: The currency of this RegisterSaleFields.  # noqa: E501
        :rtype: int
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this RegisterSaleFields.

        transaction currency in ISO numeric format  # noqa: E501

        :param currency: The currency of this RegisterSaleFields.  # noqa: E501
        :type: int
        """

        self._currency = currency

    @property
    def onetimer(self):
        """Gets the onetimer of this RegisterSaleFields.  # noqa: E501


        :return: The onetimer of this RegisterSaleFields.  # noqa: E501
        :rtype: Onetimer
        """
        return self._onetimer

    @onetimer.setter
    def onetimer(self, onetimer):
        """Sets the onetimer of this RegisterSaleFields.


        :param onetimer: The onetimer of this RegisterSaleFields.  # noqa: E501
        :type: Onetimer
        """

        self._onetimer = onetimer

    @property
    def pow_url(self):
        """Gets the pow_url of this RegisterSaleFields.  # noqa: E501

        url to redirect customer in case of payment success  # noqa: E501

        :return: The pow_url of this RegisterSaleFields.  # noqa: E501
        :rtype: str
        """
        return self._pow_url

    @pow_url.setter
    def pow_url(self, pow_url):
        """Sets the pow_url of this RegisterSaleFields.

        url to redirect customer in case of payment success  # noqa: E501

        :param pow_url: The pow_url of this RegisterSaleFields.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                pow_url is not None and len(pow_url) > 512):
            raise ValueError("Invalid value for `pow_url`, length must be less than or equal to `512`")  # noqa: E501

        self._pow_url = pow_url

    @property
    def pow_url_blad(self):
        """Gets the pow_url_blad of this RegisterSaleFields.  # noqa: E501

        url to redirect customer in case of payment failure  # noqa: E501

        :return: The pow_url_blad of this RegisterSaleFields.  # noqa: E501
        :rtype: str
        """
        return self._pow_url_blad

    @pow_url_blad.setter
    def pow_url_blad(self, pow_url_blad):
        """Sets the pow_url_blad of this RegisterSaleFields.

        url to redirect customer in case of payment failure  # noqa: E501

        :param pow_url_blad: The pow_url_blad of this RegisterSaleFields.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                pow_url_blad is not None and len(pow_url_blad) > 512):
            raise ValueError("Invalid value for `pow_url_blad`, length must be less than or equal to `512`")  # noqa: E501

        self._pow_url_blad = pow_url_blad

    @property
    def order_id(self):
        """Gets the order_id of this RegisterSaleFields.  # noqa: E501

        merchant order ID used to recognise payment  # noqa: E501

        :return: The order_id of this RegisterSaleFields.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this RegisterSaleFields.

        merchant order ID used to recognise payment  # noqa: E501

        :param order_id: The order_id of this RegisterSaleFields.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                order_id is not None and len(order_id) > 40):
            raise ValueError("Invalid value for `order_id`, length must be less than or equal to `40`")  # noqa: E501

        self._order_id = order_id

    @property
    def language(self):
        """Gets the language of this RegisterSaleFields.  # noqa: E501


        :return: The language of this RegisterSaleFields.  # noqa: E501
        :rtype: Language
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this RegisterSaleFields.


        :param language: The language of this RegisterSaleFields.  # noqa: E501
        :type: Language
        """

        self._language = language

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
        if not isinstance(other, RegisterSaleFields):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegisterSaleFields):
            return True

        return self.to_dict() != other.to_dict()