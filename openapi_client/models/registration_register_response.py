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


class RegistrationRegisterResponse(object):
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
        'seller_data': 'SellerDataObject',
        'api_data': 'ApiDataObject',
        'err': 'RegistrationErrCodes',
        'parameters': 'list[object]'
    }

    attribute_map = {
        'result': 'result',
        'seller_data': 'sellerData',
        'api_data': 'apiData',
        'err': 'err',
        'parameters': 'parameters'
    }

    def __init__(self, result=None, seller_data=None, api_data=None, err=None, parameters=None, local_vars_configuration=None):  # noqa: E501
        """RegistrationRegisterResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._result = None
        self._seller_data = None
        self._api_data = None
        self._err = None
        self._parameters = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if seller_data is not None:
            self.seller_data = seller_data
        if api_data is not None:
            self.api_data = api_data
        if err is not None:
            self.err = err
        if parameters is not None:
            self.parameters = parameters

    @property
    def result(self):
        """Gets the result of this RegistrationRegisterResponse.  # noqa: E501


        :return: The result of this RegistrationRegisterResponse.  # noqa: E501
        :rtype: Result
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this RegistrationRegisterResponse.


        :param result: The result of this RegistrationRegisterResponse.  # noqa: E501
        :type: Result
        """

        self._result = result

    @property
    def seller_data(self):
        """Gets the seller_data of this RegistrationRegisterResponse.  # noqa: E501


        :return: The seller_data of this RegistrationRegisterResponse.  # noqa: E501
        :rtype: SellerDataObject
        """
        return self._seller_data

    @seller_data.setter
    def seller_data(self, seller_data):
        """Sets the seller_data of this RegistrationRegisterResponse.


        :param seller_data: The seller_data of this RegistrationRegisterResponse.  # noqa: E501
        :type: SellerDataObject
        """

        self._seller_data = seller_data

    @property
    def api_data(self):
        """Gets the api_data of this RegistrationRegisterResponse.  # noqa: E501


        :return: The api_data of this RegistrationRegisterResponse.  # noqa: E501
        :rtype: ApiDataObject
        """
        return self._api_data

    @api_data.setter
    def api_data(self, api_data):
        """Sets the api_data of this RegistrationRegisterResponse.


        :param api_data: The api_data of this RegistrationRegisterResponse.  # noqa: E501
        :type: ApiDataObject
        """

        self._api_data = api_data

    @property
    def err(self):
        """Gets the err of this RegistrationRegisterResponse.  # noqa: E501


        :return: The err of this RegistrationRegisterResponse.  # noqa: E501
        :rtype: RegistrationErrCodes
        """
        return self._err

    @err.setter
    def err(self, err):
        """Sets the err of this RegistrationRegisterResponse.


        :param err: The err of this RegistrationRegisterResponse.  # noqa: E501
        :type: RegistrationErrCodes
        """

        self._err = err

    @property
    def parameters(self):
        """Gets the parameters of this RegistrationRegisterResponse.  # noqa: E501


        :return: The parameters of this RegistrationRegisterResponse.  # noqa: E501
        :rtype: list[object]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this RegistrationRegisterResponse.


        :param parameters: The parameters of this RegistrationRegisterResponse.  # noqa: E501
        :type: list[object]
        """

        self._parameters = parameters

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
        if not isinstance(other, RegistrationRegisterResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegistrationRegisterResponse):
            return True

        return self.to_dict() != other.to_dict()