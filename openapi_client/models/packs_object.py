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


class PacksObject(object):
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
        'pack_id': 'int',
        'date': 'str',
        'auth_date': 'str',
        'status': 'str',
        'count': 'int',
        'sum': 'float',
        'cost': 'float'
    }

    attribute_map = {
        'pack_id': 'pack_id',
        'date': 'date',
        'auth_date': 'auth_date',
        'status': 'status',
        'count': 'count',
        'sum': 'sum',
        'cost': 'cost'
    }

    def __init__(self, pack_id=None, date=None, auth_date=None, status=None, count=None, sum=None, cost=None, local_vars_configuration=None):  # noqa: E501
        """PacksObject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pack_id = None
        self._date = None
        self._auth_date = None
        self._status = None
        self._count = None
        self._sum = None
        self._cost = None
        self.discriminator = None

        if pack_id is not None:
            self.pack_id = pack_id
        if date is not None:
            self.date = date
        if auth_date is not None:
            self.auth_date = auth_date
        if status is not None:
            self.status = status
        if count is not None:
            self.count = count
        if sum is not None:
            self.sum = sum
        if cost is not None:
            self.cost = cost

    @property
    def pack_id(self):
        """Gets the pack_id of this PacksObject.  # noqa: E501

        ID of created pack using method create.  # noqa: E501

        :return: The pack_id of this PacksObject.  # noqa: E501
        :rtype: int
        """
        return self._pack_id

    @pack_id.setter
    def pack_id(self, pack_id):
        """Sets the pack_id of this PacksObject.

        ID of created pack using method create.  # noqa: E501

        :param pack_id: The pack_id of this PacksObject.  # noqa: E501
        :type: int
        """

        self._pack_id = pack_id

    @property
    def date(self):
        """Gets the date of this PacksObject.  # noqa: E501

        Date of package creation  # noqa: E501

        :return: The date of this PacksObject.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this PacksObject.

        Date of package creation  # noqa: E501

        :param date: The date of this PacksObject.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                date is not None and not re.search(r'YYYY-MM-DD HH:mm:ss', date)):  # noqa: E501
            raise ValueError(r"Invalid value for `date`, must be a follow pattern or equal to `/YYYY-MM-DD HH:mm:ss/`")  # noqa: E501

        self._date = date

    @property
    def auth_date(self):
        """Gets the auth_date of this PacksObject.  # noqa: E501

        Date of package authorization (method authorize)  # noqa: E501

        :return: The auth_date of this PacksObject.  # noqa: E501
        :rtype: str
        """
        return self._auth_date

    @auth_date.setter
    def auth_date(self, auth_date):
        """Sets the auth_date of this PacksObject.

        Date of package authorization (method authorize)  # noqa: E501

        :param auth_date: The auth_date of this PacksObject.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                auth_date is not None and not re.search(r'YYYY-MM-DD HH:mm:ss', auth_date)):  # noqa: E501
            raise ValueError(r"Invalid value for `auth_date`, must be a follow pattern or equal to `/YYYY-MM-DD HH:mm:ss/`")  # noqa: E501

        self._auth_date = auth_date

    @property
    def status(self):
        """Gets the status of this PacksObject.  # noqa: E501

        Package status  # noqa: E501

        :return: The status of this PacksObject.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PacksObject.

        Package status  # noqa: E501

        :param status: The status of this PacksObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "auth"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def count(self):
        """Gets the count of this PacksObject.  # noqa: E501

        Number of transfers in the package  # noqa: E501

        :return: The count of this PacksObject.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PacksObject.

        Number of transfers in the package  # noqa: E501

        :param count: The count of this PacksObject.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def sum(self):
        """Gets the sum of this PacksObject.  # noqa: E501

        Sum of transfers in the package  # noqa: E501

        :return: The sum of this PacksObject.  # noqa: E501
        :rtype: float
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """Sets the sum of this PacksObject.

        Sum of transfers in the package  # noqa: E501

        :param sum: The sum of this PacksObject.  # noqa: E501
        :type: float
        """

        self._sum = sum

    @property
    def cost(self):
        """Gets the cost of this PacksObject.  # noqa: E501

        Additional cost of processing transfers in the package   # noqa: E501

        :return: The cost of this PacksObject.  # noqa: E501
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this PacksObject.

        Additional cost of processing transfers in the package   # noqa: E501

        :param cost: The cost of this PacksObject.  # noqa: E501
        :type: float
        """

        self._cost = cost

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
        if not isinstance(other, PacksObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PacksObject):
            return True

        return self.to_dict() != other.to_dict()
