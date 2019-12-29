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


class CreateFields(object):
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
        'id': 'int',
        'amount': 'float',
        'description': 'str',
        'crc': 'str',
        'md5sum': 'str',
        'group': 'int',
        'result_url': 'str',
        'result_email': 'str',
        'merchant_description': 'str',
        'custom_description': 'str',
        'return_url': 'str',
        'return_error_url': 'str',
        'language': 'str',
        'email': 'str',
        'name': 'str',
        'address': 'str',
        'city': 'str',
        'zip': 'str',
        'country': 'str',
        'phone': 'str',
        'accept_tos': 'int',
        'api_password': 'str'
    }

    attribute_map = {
        'id': 'id',
        'amount': 'amount',
        'description': 'description',
        'crc': 'crc',
        'md5sum': 'md5sum',
        'group': 'group',
        'result_url': 'result_url',
        'result_email': 'result_email',
        'merchant_description': 'merchant_description',
        'custom_description': 'custom_description',
        'return_url': 'return_url',
        'return_error_url': 'return_error_url',
        'language': 'language',
        'email': 'email',
        'name': 'name',
        'address': 'address',
        'city': 'city',
        'zip': 'zip',
        'country': 'country',
        'phone': 'phone',
        'accept_tos': 'accept_tos',
        'api_password': 'api_password'
    }

    def __init__(self, id=None, amount=None, description=None, crc=None, md5sum=None, group=None, result_url=None, result_email=None, merchant_description=None, custom_description=None, return_url=None, return_error_url=None, language='pl', email=None, name=None, address=None, city=None, zip=None, country=None, phone=None, accept_tos=None, api_password=None, local_vars_configuration=None):  # noqa: E501
        """CreateFields - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._amount = None
        self._description = None
        self._crc = None
        self._md5sum = None
        self._group = None
        self._result_url = None
        self._result_email = None
        self._merchant_description = None
        self._custom_description = None
        self._return_url = None
        self._return_error_url = None
        self._language = None
        self._email = None
        self._name = None
        self._address = None
        self._city = None
        self._zip = None
        self._country = None
        self._phone = None
        self._accept_tos = None
        self._api_password = None
        self.discriminator = None

        self.id = id
        self.amount = amount
        self.description = description
        if crc is not None:
            self.crc = crc
        self.md5sum = md5sum
        self.group = group
        if result_url is not None:
            self.result_url = result_url
        if result_email is not None:
            self.result_email = result_email
        if merchant_description is not None:
            self.merchant_description = merchant_description
        if custom_description is not None:
            self.custom_description = custom_description
        if return_url is not None:
            self.return_url = return_url
        if return_error_url is not None:
            self.return_error_url = return_error_url
        if language is not None:
            self.language = language
        self.email = email
        self.name = name
        if address is not None:
            self.address = address
        if city is not None:
            self.city = city
        if zip is not None:
            self.zip = zip
        if country is not None:
            self.country = country
        if phone is not None:
            self.phone = phone
        if accept_tos is not None:
            self.accept_tos = accept_tos
        self.api_password = api_password

    @property
    def id(self):
        """Gets the id of this CreateFields.  # noqa: E501

        Merchant ID in Tpay.com system  # noqa: E501

        :return: The id of this CreateFields.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateFields.

        Merchant ID in Tpay.com system  # noqa: E501

        :param id: The id of this CreateFields.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def amount(self):
        """Gets the amount of this CreateFields.  # noqa: E501

        Transaction amount. Please always send the amount with two decimal places like 10.00  # noqa: E501

        :return: The amount of this CreateFields.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreateFields.

        Transaction amount. Please always send the amount with two decimal places like 10.00  # noqa: E501

        :param amount: The amount of this CreateFields.  # noqa: E501
        :type: float
        """
        #if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
        #    raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501
        #if (self.local_vars_configuration.client_side_validation and
        #        amount is not None and amount < 0.01):  # noqa: E501
        #    raise ValueError("Invalid value for `amount`, must be a value greater than or equal to `0.01`")  # noqa: E501

        self._amount = amount

    @property
    def description(self):
        """Gets the description of this CreateFields.  # noqa: E501

        Transaction description  # noqa: E501

        :return: The description of this CreateFields.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateFields.

        Transaction description  # noqa: E501

        :param description: The description of this CreateFields.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 128):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `128`")  # noqa: E501

        self._description = description

    @property
    def crc(self):
        """Gets the crc of this CreateFields.  # noqa: E501

        Auxiliary parameter to identify the transaction on the merchant side. We do recommend to encode your crc value in base64. The exact value of crc used to create transaction will be returned in tpay payment notification as tr_crc parameter.  # noqa: E501

        :return: The crc of this CreateFields.  # noqa: E501
        :rtype: str
        """
        return self._crc

    @crc.setter
    def crc(self, crc):
        """Sets the crc of this CreateFields.

        Auxiliary parameter to identify the transaction on the merchant side. We do recommend to encode your crc value in base64. The exact value of crc used to create transaction will be returned in tpay payment notification as tr_crc parameter.  # noqa: E501

        :param crc: The crc of this CreateFields.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                crc is not None and len(crc) > 128):
            raise ValueError("Invalid value for `crc`, length must be less than or equal to `128`")  # noqa: E501

        self._crc = crc

    @property
    def md5sum(self):
        """Gets the md5sum of this CreateFields.  # noqa: E501

        md5 sum calculated from id.amount.crc.security_code where dots means concatenation (security code can be found in merchant panel).  # noqa: E501

        :return: The md5sum of this CreateFields.  # noqa: E501
        :rtype: str
        """
        return self._md5sum

    @md5sum.setter
    def md5sum(self, md5sum):
        """Sets the md5sum of this CreateFields.

        md5 sum calculated from id.amount.crc.security_code where dots means concatenation (security code can be found in merchant panel).  # noqa: E501

        :param md5sum: The md5sum of this CreateFields.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and md5sum is None:  # noqa: E501
            raise ValueError("Invalid value for `md5sum`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                md5sum is not None and len(md5sum) > 32):
            raise ValueError("Invalid value for `md5sum`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                md5sum is not None and len(md5sum) < 32):
            raise ValueError("Invalid value for `md5sum`, length must be greater than or equal to `32`")  # noqa: E501

        self._md5sum = md5sum

    @property
    def group(self):
        """Gets the group of this CreateFields.  # noqa: E501

        Transaction group number see the \"id\" element in https://secure.tpay.com/groups-{id}0.js . For example https://secure.tpay.com/groups-10100.js or https://secure.tpay.com/groups-10100.js?json  # noqa: E501

        :return: The group of this CreateFields.  # noqa: E501
        :rtype: int
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this CreateFields.

        Transaction group number see the \"id\" element in https://secure.tpay.com/groups-{id}0.js . For example https://secure.tpay.com/groups-10100.js or https://secure.tpay.com/groups-10100.js?json  # noqa: E501

        :param group: The group of this CreateFields.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and group is None:  # noqa: E501
            raise ValueError("Invalid value for `group`, must not be `None`")  # noqa: E501

        self._group = group

    @property
    def result_url(self):
        """Gets the result_url of this CreateFields.  # noqa: E501

        Merchant endpoint for payment notification  # noqa: E501

        :return: The result_url of this CreateFields.  # noqa: E501
        :rtype: str
        """
        return self._result_url

    @result_url.setter
    def result_url(self, result_url):
        """Sets the result_url of this CreateFields.

        Merchant endpoint for payment notification  # noqa: E501

        :param result_url: The result_url of this CreateFields.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                result_url is not None and len(result_url) > 512):
            raise ValueError("Invalid value for `result_url`, length must be less than or equal to `512`")  # noqa: E501

        self._result_url = result_url

    @property
    def result_email(self):
        """Gets the result_email of this CreateFields.  # noqa: E501

        Email address where notification after payment will be sent (overrides defined in merchant panel). You can add more addresses by comma concatenation.  # noqa: E501

        :return: The result_email of this CreateFields.  # noqa: E501
        :rtype: str
        """
        return self._result_email

    @result_email.setter
    def result_email(self, result_email):
        """Sets the result_email of this CreateFields.

        Email address where notification after payment will be sent (overrides defined in merchant panel). You can add more addresses by comma concatenation.  # noqa: E501

        :param result_email: The result_email of this CreateFields.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                result_email is not None and len(result_email) > 256):
            raise ValueError("Invalid value for `result_email`, length must be less than or equal to `256`")  # noqa: E501

        self._result_email = result_email

    @property
    def merchant_description(self):
        """Gets the merchant_description of this CreateFields.  # noqa: E501

        Name of merchant displayed in transaction panel (overrides defined in merchant panel)  # noqa: E501

        :return: The merchant_description of this CreateFields.  # noqa: E501
        :rtype: str
        """
        return self._merchant_description

    @merchant_description.setter
    def merchant_description(self, merchant_description):
        """Sets the merchant_description of this CreateFields.

        Name of merchant displayed in transaction panel (overrides defined in merchant panel)  # noqa: E501

        :param merchant_description: The merchant_description of this CreateFields.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                merchant_description is not None and len(merchant_description) > 128):
            raise ValueError("Invalid value for `merchant_description`, length must be less than or equal to `128`")  # noqa: E501

        self._merchant_description = merchant_description

    @property
    def custom_description(self):
        """Gets the custom_description of this CreateFields.  # noqa: E501

        Additional info to be displayed in transaction panel (overrides defined in merchant panel)  # noqa: E501

        :return: The custom_description of this CreateFields.  # noqa: E501
        :rtype: str
        """
        return self._custom_description

    @custom_description.setter
    def custom_description(self, custom_description):
        """Sets the custom_description of this CreateFields.

        Additional info to be displayed in transaction panel (overrides defined in merchant panel)  # noqa: E501

        :param custom_description: The custom_description of this CreateFields.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                custom_description is not None and len(custom_description) > 32):
            raise ValueError("Invalid value for `custom_description`, length must be less than or equal to `32`")  # noqa: E501

        self._custom_description = custom_description

    @property
    def return_url(self):
        """Gets the return_url of this CreateFields.  # noqa: E501

        url to redirect customer in case of payment success  # noqa: E501

        :return: The return_url of this CreateFields.  # noqa: E501
        :rtype: str
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """Sets the return_url of this CreateFields.

        url to redirect customer in case of payment success  # noqa: E501

        :param return_url: The return_url of this CreateFields.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                return_url is not None and len(return_url) > 512):
            raise ValueError("Invalid value for `return_url`, length must be less than or equal to `512`")  # noqa: E501

        self._return_url = return_url

    @property
    def return_error_url(self):
        """Gets the return_error_url of this CreateFields.  # noqa: E501

        url to redirect customer in case of payment failure  # noqa: E501

        :return: The return_error_url of this CreateFields.  # noqa: E501
        :rtype: str
        """
        return self._return_error_url

    @return_error_url.setter
    def return_error_url(self, return_error_url):
        """Sets the return_error_url of this CreateFields.

        url to redirect customer in case of payment failure  # noqa: E501

        :param return_error_url: The return_error_url of this CreateFields.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                return_error_url is not None and len(return_error_url) > 512):
            raise ValueError("Invalid value for `return_error_url`, length must be less than or equal to `512`")  # noqa: E501

        self._return_error_url = return_error_url

    @property
    def language(self):
        """Gets the language of this CreateFields.  # noqa: E501

        Customer language  # noqa: E501

        :return: The language of this CreateFields.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this CreateFields.

        Customer language  # noqa: E501

        :param language: The language of this CreateFields.  # noqa: E501
        :type: str
        """
        allowed_values = ["pl", "en", "de"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and language not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"  # noqa: E501
                .format(language, allowed_values)
            )

        self._language = language

    @property
    def email(self):
        """Gets the email of this CreateFields.  # noqa: E501

        customer email  # noqa: E501

        :return: The email of this CreateFields.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateFields.

        customer email  # noqa: E501

        :param email: The email of this CreateFields.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 64):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `64`")  # noqa: E501

        self._email = email

    @property
    def name(self):
        """Gets the name of this CreateFields.  # noqa: E501

        customer name  # noqa: E501

        :return: The name of this CreateFields.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateFields.

        customer name  # noqa: E501

        :param name: The name of this CreateFields.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 64):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501

        self._name = name

    @property
    def address(self):
        """Gets the address of this CreateFields.  # noqa: E501

        customer address (parameter is empty if this field was not send with create method)  # noqa: E501

        :return: The address of this CreateFields.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CreateFields.

        customer address (parameter is empty if this field was not send with create method)  # noqa: E501

        :param address: The address of this CreateFields.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def city(self):
        """Gets the city of this CreateFields.  # noqa: E501

        customer city (parameter is empty if this field was not send with create method)  # noqa: E501

        :return: The city of this CreateFields.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CreateFields.

        customer city (parameter is empty if this field was not send with create method)  # noqa: E501

        :param city: The city of this CreateFields.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def zip(self):
        """Gets the zip of this CreateFields.  # noqa: E501

        customer postal code (parameter is empty if this field was not send with create method)  # noqa: E501

        :return: The zip of this CreateFields.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this CreateFields.

        customer postal code (parameter is empty if this field was not send with create method)  # noqa: E501

        :param zip: The zip of this CreateFields.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def country(self):
        """Gets the country of this CreateFields.  # noqa: E501

        Two letters - see ISO 3166-1 document  # noqa: E501

        :return: The country of this CreateFields.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CreateFields.

        Two letters - see ISO 3166-1 document  # noqa: E501

        :param country: The country of this CreateFields.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def phone(self):
        """Gets the phone of this CreateFields.  # noqa: E501

        customer phone number (parameter is empty if this field was not send with create method)  # noqa: E501

        :return: The phone of this CreateFields.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CreateFields.

        customer phone number (parameter is empty if this field was not send with create method)  # noqa: E501

        :param phone: The phone of this CreateFields.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def accept_tos(self):
        """Gets the accept_tos of this CreateFields.  # noqa: E501

        Acceptance of Tpay.com regulations done by customer on Merchant site  # noqa: E501

        :return: The accept_tos of this CreateFields.  # noqa: E501
        :rtype: int
        """
        return self._accept_tos

    @accept_tos.setter
    def accept_tos(self, accept_tos):
        """Sets the accept_tos of this CreateFields.

        Acceptance of Tpay.com regulations done by customer on Merchant site  # noqa: E501

        :param accept_tos: The accept_tos of this CreateFields.  # noqa: E501
        :type: int
        """

        self._accept_tos = accept_tos

    @property
    def api_password(self):
        """Gets the api_password of this CreateFields.  # noqa: E501

        API password.  # noqa: E501

        :return: The api_password of this CreateFields.  # noqa: E501
        :rtype: str
        """
        return self._api_password

    @api_password.setter
    def api_password(self, api_password):
        """Sets the api_password of this CreateFields.

        API password.  # noqa: E501

        :param api_password: The api_password of this CreateFields.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and api_password is None:  # noqa: E501
            raise ValueError("Invalid value for `api_password`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                api_password is not None and len(api_password) > 40):
            raise ValueError("Invalid value for `api_password`, length must be less than or equal to `40`")  # noqa: E501

        self._api_password = api_password

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
        if not isinstance(other, CreateFields):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateFields):
            return True

        return self.to_dict() != other.to_dict()
