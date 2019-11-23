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


class RegistrationInputsResponse(object):
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
        'legal_forms': 'list[LegalFormObject]',
        'branches': 'list[BranchObject]',
        'err': 'RegistrationErrCodes'
    }

    attribute_map = {
        'result': 'result',
        'legal_forms': 'legalForms',
        'branches': 'branches',
        'err': 'err'
    }

    def __init__(self, result=None, legal_forms=None, branches=None, err=None, local_vars_configuration=None):  # noqa: E501
        """RegistrationInputsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._result = None
        self._legal_forms = None
        self._branches = None
        self._err = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if legal_forms is not None:
            self.legal_forms = legal_forms
        if branches is not None:
            self.branches = branches
        if err is not None:
            self.err = err

    @property
    def result(self):
        """Gets the result of this RegistrationInputsResponse.  # noqa: E501


        :return: The result of this RegistrationInputsResponse.  # noqa: E501
        :rtype: Result
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this RegistrationInputsResponse.


        :param result: The result of this RegistrationInputsResponse.  # noqa: E501
        :type: Result
        """

        self._result = result

    @property
    def legal_forms(self):
        """Gets the legal_forms of this RegistrationInputsResponse.  # noqa: E501


        :return: The legal_forms of this RegistrationInputsResponse.  # noqa: E501
        :rtype: list[LegalFormObject]
        """
        return self._legal_forms

    @legal_forms.setter
    def legal_forms(self, legal_forms):
        """Sets the legal_forms of this RegistrationInputsResponse.


        :param legal_forms: The legal_forms of this RegistrationInputsResponse.  # noqa: E501
        :type: list[LegalFormObject]
        """

        self._legal_forms = legal_forms

    @property
    def branches(self):
        """Gets the branches of this RegistrationInputsResponse.  # noqa: E501


        :return: The branches of this RegistrationInputsResponse.  # noqa: E501
        :rtype: list[BranchObject]
        """
        return self._branches

    @branches.setter
    def branches(self, branches):
        """Sets the branches of this RegistrationInputsResponse.


        :param branches: The branches of this RegistrationInputsResponse.  # noqa: E501
        :type: list[BranchObject]
        """

        self._branches = branches

    @property
    def err(self):
        """Gets the err of this RegistrationInputsResponse.  # noqa: E501


        :return: The err of this RegistrationInputsResponse.  # noqa: E501
        :rtype: RegistrationErrCodes
        """
        return self._err

    @err.setter
    def err(self, err):
        """Sets the err of this RegistrationInputsResponse.


        :param err: The err of this RegistrationInputsResponse.  # noqa: E501
        :type: RegistrationErrCodes
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
        if not isinstance(other, RegistrationInputsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegistrationInputsResponse):
            return True

        return self.to_dict() != other.to_dict()