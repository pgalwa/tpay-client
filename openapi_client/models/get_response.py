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


class GetResponse(object):
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
        'status': 'str',
        'error_code': 'str',
        'start_time': 'str',
        'payment_time': 'str',
        'chargeback_time': 'str',
        'channel': 'int',
        'test_mode': 'int',
        'amount': 'float',
        'amount_paid': 'float',
        'name': 'str',
        'email': 'str',
        'address': 'str',
        'code': 'str',
        'city': 'str',
        'phone': 'str',
        'country': 'str',
        'err': 'TransactionErrorCodes'
    }

    attribute_map = {
        'result': 'result',
        'status': 'status',
        'error_code': 'error_code',
        'start_time': 'start_time',
        'payment_time': 'payment_time',
        'chargeback_time': 'chargeback_time',
        'channel': 'channel',
        'test_mode': 'test_mode',
        'amount': 'amount',
        'amount_paid': 'amount_paid',
        'name': 'name',
        'email': 'email',
        'address': 'address',
        'code': 'code',
        'city': 'city',
        'phone': 'phone',
        'country': 'country',
        'err': 'err'
    }

    def __init__(self, result=None, status=None, error_code=None, start_time=None, payment_time=None, chargeback_time=None, channel=None, test_mode=None, amount=None, amount_paid=None, name=None, email=None, address=None, code=None, city=None, phone=None, country=None, err=None, local_vars_configuration=None):  # noqa: E501
        """GetResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._result = None
        self._status = None
        self._error_code = None
        self._start_time = None
        self._payment_time = None
        self._chargeback_time = None
        self._channel = None
        self._test_mode = None
        self._amount = None
        self._amount_paid = None
        self._name = None
        self._email = None
        self._address = None
        self._code = None
        self._city = None
        self._phone = None
        self._country = None
        self._err = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if status is not None:
            self.status = status
        if error_code is not None:
            self.error_code = error_code
        if start_time is not None:
            self.start_time = start_time
        if payment_time is not None:
            self.payment_time = payment_time
        if chargeback_time is not None:
            self.chargeback_time = chargeback_time
        if channel is not None:
            self.channel = channel
        if test_mode is not None:
            self.test_mode = test_mode
        if amount is not None:
            self.amount = amount
        if amount_paid is not None:
            self.amount_paid = amount_paid
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if address is not None:
            self.address = address
        if code is not None:
            self.code = code
        if city is not None:
            self.city = city
        if phone is not None:
            self.phone = phone
        if country is not None:
            self.country = country
        if err is not None:
            self.err = err

    @property
    def result(self):
        """Gets the result of this GetResponse.  # noqa: E501


        :return: The result of this GetResponse.  # noqa: E501
        :rtype: Result
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this GetResponse.


        :param result: The result of this GetResponse.  # noqa: E501
        :type: Result
        """

        self._result = result

    @property
    def status(self):
        """Gets the status of this GetResponse.  # noqa: E501


        :return: The status of this GetResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetResponse.


        :param status: The status of this GetResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["correct", "paid", "pending", "error", "chargeback"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def error_code(self):
        """Gets the error_code of this GetResponse.  # noqa: E501

        Depending on setting in merchant panel, error_code may be different than none for correct status, when acceptance of overpays and surcharges has been set.  # noqa: E501

        :return: The error_code of this GetResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this GetResponse.

        Depending on setting in merchant panel, error_code may be different than none for correct status, when acceptance of overpays and surcharges has been set.  # noqa: E501

        :param error_code: The error_code of this GetResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "overpay", "surcharge"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and error_code not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `error_code` ({0}), must be one of {1}"  # noqa: E501
                .format(error_code, allowed_values)
            )

        self._error_code = error_code

    @property
    def start_time(self):
        """Gets the start_time of this GetResponse.  # noqa: E501

        Transaction creation time  # noqa: E501

        :return: The start_time of this GetResponse.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this GetResponse.

        Transaction creation time  # noqa: E501

        :param start_time: The start_time of this GetResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                start_time is not None and not re.search(r'YYYY-MM-DD HH:mm:ss', start_time)):  # noqa: E501
            raise ValueError(r"Invalid value for `start_time`, must be a follow pattern or equal to `/YYYY-MM-DD HH:mm:ss/`")  # noqa: E501

        self._start_time = start_time

    @property
    def payment_time(self):
        """Gets the payment_time of this GetResponse.  # noqa: E501

        Date of payment or empty for pending transactions  # noqa: E501

        :return: The payment_time of this GetResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_time

    @payment_time.setter
    def payment_time(self, payment_time):
        """Sets the payment_time of this GetResponse.

        Date of payment or empty for pending transactions  # noqa: E501

        :param payment_time: The payment_time of this GetResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                payment_time is not None and not re.search(r'YYYY-MM-DD HH:mm:ss', payment_time)):  # noqa: E501
            raise ValueError(r"Invalid value for `payment_time`, must be a follow pattern or equal to `/YYYY-MM-DD HH:mm:ss/`")  # noqa: E501

        self._payment_time = payment_time

    @property
    def chargeback_time(self):
        """Gets the chargeback_time of this GetResponse.  # noqa: E501

        Date of payment refund or empty for not refunded transactions  # noqa: E501

        :return: The chargeback_time of this GetResponse.  # noqa: E501
        :rtype: str
        """
        return self._chargeback_time

    @chargeback_time.setter
    def chargeback_time(self, chargeback_time):
        """Sets the chargeback_time of this GetResponse.

        Date of payment refund or empty for not refunded transactions  # noqa: E501

        :param chargeback_time: The chargeback_time of this GetResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                chargeback_time is not None and not re.search(r'YYYY-MM-DD HH:mm:ss', chargeback_time)):  # noqa: E501
            raise ValueError(r"Invalid value for `chargeback_time`, must be a follow pattern or equal to `/YYYY-MM-DD HH:mm:ss/`")  # noqa: E501

        self._chargeback_time = chargeback_time

    @property
    def channel(self):
        """Gets the channel of this GetResponse.  # noqa: E501

        Payment channel ID can be recognised in merchant panel (your offer section)  # noqa: E501

        :return: The channel of this GetResponse.  # noqa: E501
        :rtype: int
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this GetResponse.

        Payment channel ID can be recognised in merchant panel (your offer section)  # noqa: E501

        :param channel: The channel of this GetResponse.  # noqa: E501
        :type: int
        """

        self._channel = channel

    @property
    def test_mode(self):
        """Gets the test_mode of this GetResponse.  # noqa: E501

        Returns 1 if transaction was in test mode  # noqa: E501

        :return: The test_mode of this GetResponse.  # noqa: E501
        :rtype: int
        """
        return self._test_mode

    @test_mode.setter
    def test_mode(self, test_mode):
        """Sets the test_mode of this GetResponse.

        Returns 1 if transaction was in test mode  # noqa: E501

        :param test_mode: The test_mode of this GetResponse.  # noqa: E501
        :type: int
        """

        self._test_mode = test_mode

    @property
    def amount(self):
        """Gets the amount of this GetResponse.  # noqa: E501

        transaction amount casted to float  # noqa: E501

        :return: The amount of this GetResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this GetResponse.

        transaction amount casted to float  # noqa: E501

        :param amount: The amount of this GetResponse.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                amount is not None and amount < 0.1):  # noqa: E501
            raise ValueError("Invalid value for `amount`, must be a value greater than or equal to `0.1`")  # noqa: E501

        self._amount = amount

    @property
    def amount_paid(self):
        """Gets the amount_paid of this GetResponse.  # noqa: E501

        The amount paid by customer  # noqa: E501

        :return: The amount_paid of this GetResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount_paid

    @amount_paid.setter
    def amount_paid(self, amount_paid):
        """Sets the amount_paid of this GetResponse.

        The amount paid by customer  # noqa: E501

        :param amount_paid: The amount_paid of this GetResponse.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                amount_paid is not None and amount_paid < 0.01):  # noqa: E501
            raise ValueError("Invalid value for `amount_paid`, must be a value greater than or equal to `0.01`")  # noqa: E501

        self._amount_paid = amount_paid

    @property
    def name(self):
        """Gets the name of this GetResponse.  # noqa: E501

        customer name  # noqa: E501

        :return: The name of this GetResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetResponse.

        customer name  # noqa: E501

        :param name: The name of this GetResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 64):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501

        self._name = name

    @property
    def email(self):
        """Gets the email of this GetResponse.  # noqa: E501

        customer email  # noqa: E501

        :return: The email of this GetResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GetResponse.

        customer email  # noqa: E501

        :param email: The email of this GetResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 64):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `64`")  # noqa: E501

        self._email = email

    @property
    def address(self):
        """Gets the address of this GetResponse.  # noqa: E501

        customer address (parameter is empty if this field was not send with create method)  # noqa: E501

        :return: The address of this GetResponse.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this GetResponse.

        customer address (parameter is empty if this field was not send with create method)  # noqa: E501

        :param address: The address of this GetResponse.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def code(self):
        """Gets the code of this GetResponse.  # noqa: E501

        customer postal code (parameter is empty if this field was not send with create method)  # noqa: E501

        :return: The code of this GetResponse.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this GetResponse.

        customer postal code (parameter is empty if this field was not send with create method)  # noqa: E501

        :param code: The code of this GetResponse.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def city(self):
        """Gets the city of this GetResponse.  # noqa: E501

        customer city (parameter is empty if this field was not send with create method)  # noqa: E501

        :return: The city of this GetResponse.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this GetResponse.

        customer city (parameter is empty if this field was not send with create method)  # noqa: E501

        :param city: The city of this GetResponse.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def phone(self):
        """Gets the phone of this GetResponse.  # noqa: E501

        customer phone number (parameter is empty if this field was not send with create method)  # noqa: E501

        :return: The phone of this GetResponse.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this GetResponse.

        customer phone number (parameter is empty if this field was not send with create method)  # noqa: E501

        :param phone: The phone of this GetResponse.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def country(self):
        """Gets the country of this GetResponse.  # noqa: E501

        Two letters - see ISO 3166-1 document  # noqa: E501

        :return: The country of this GetResponse.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this GetResponse.

        Two letters - see ISO 3166-1 document  # noqa: E501

        :param country: The country of this GetResponse.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def err(self):
        """Gets the err of this GetResponse.  # noqa: E501


        :return: The err of this GetResponse.  # noqa: E501
        :rtype: TransactionErrorCodes
        """
        return self._err

    @err.setter
    def err(self, err):
        """Sets the err of this GetResponse.


        :param err: The err of this GetResponse.  # noqa: E501
        :type: TransactionErrorCodes
        """

        self._err = err

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
        if not isinstance(other, GetResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetResponse):
            return True

        return self.to_dict() != other.to_dict()
