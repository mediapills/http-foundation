# Copyright (c) 2021-2021 Mediapills HttpFoundation.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import abc
import typing as t
from enum import Enum


# Successful responses codes group

"""The request succeeded."""
HTTP_CODE_OK = 200

"""The request succeeded, and a new resource created as a result."""
HTTP_CODE_CREATED = 201

"""The request has been received but not yet acted upon. It is noncommittal, since
there is no way in HTTP to later send an asynchronous response indicating the
outcome of the request."""
HTTP_CODE_ACCEPTED = 202

"""This response code means the returned metadata is not exactly the same as is
available from the origin server, but is collected from a local or a third-party
copy."""
HTTP_CODE_NON_AUTHORITATIVE_INFORMATION = 203

"""There is no content to send for this request, but the headers may be useful."""
HTTP_CODE_NO_CONTENT = 204

"""Tells the user agent to reset the document which sent this request."""
HTTP_CODE_RESET_CONTENT = 205

"""This response code is used when the Range header is sent from the client to request
only part of a resource."""
HTTP_CODE_PARTIAL_CONTENT = 206

"""Conveys information about multiple resources, for situations where multiple status
codes might be appropriate."""
HTTP_CODE_MULTI_STATUS = 207

"""Used inside a <dav:propstat> response element to avoid repeatedly enumerating the
internal members of multiple bindings to the same collection."""
HTTP_CODE_ALREADY_REPORTED = 208

"""The server has fulfilled a GET request for the resource, and the response is a
representation of the result of one or more instance-manipulations applied to the current
instance."""
HTTP_CODE_IM_USED = 226

# Redirection messages responses codes group

"""The request has more than one possible response."""
HTTP_CODE_MULTIPLE_CHOICES = 300

"""The URL of the requested resource has been changed permanently."""
HTTP_CODE_MOVED_PERMANENTLY = 301

"""This response code means that the URI of requested resource has been changed
temporarily.
"""
HTTP_CODE_FOUND = 302

"""The server sent this response to direct the client to get the requested resource at
another URI with a GET request."""
HTTP_CODE_SEE_OTHER = 303

"""This is used for caching purposes. It tells the client that the response has not been
modified, so the client can continue to use the same cached version of the response."""
HTTP_CODE_NOT_MODIFIED = 304

"""Defined in a previous version of the HTTP specification to indicate that a requested
response must be accessed by a proxy."""
HTTP_CODE_USE_PROXY = 305

"""The server sends this response to direct the client to get the requested resource at
another URI with same method that was used in the prior request."""
HTTP_CODE_TEMPORARY_REDIRECT = 307

"""This means that the resource is now permanently located at another URI, specified by
the Location: HTTP Response header."""
HTTP_CODE_PERMANENT_REDIRECT = 308

# Client error responses codes group

"""The server could not understand the request due to invalid syntax."""
HTTP_CODE_BAD_REQUEST = 400

"""Although the HTTP standard specifies 'unauthorized', semantically this
response means 'unauthenticated'.
"""
HTTP_CODE_UNAUTHORIZED = 401

"""The client does not have access rights to the content; that is, it is
unauthorized, so the server is refusing to give the requested resource.
"""
HTTP_CODE_FORBIDDEN = 403

"""The server can not find the requested resource. In the browser, this means
the URL is not recognized.
"""
HTTP_CODE_NOT_FOUND = 404

"""This response is sent when a request conflicts with the current state of the
server.
"""
HTTP_CODE_CONFLICT = 409

"""The request was well-formed but was unable to be followed due to semantic errors."""
HTTP_CODE_UNPROCESSABLE_ENTITY = 422

# Server error responses codes group

"""The server has encountered a situation it does not know how to handle."""
HTTP_CODE_INTERNAL_SERVER_ERROR = 500


class HTTPStatusCode(Enum):
    """Enumerated HTTP response codes constants."""

    OK = HTTP_CODE_OK
    CREATED = HTTP_CODE_CREATED
    ACCEPTED = HTTP_CODE_ACCEPTED
    NON_AUTHORITATIVE_INFORMATION = HTTP_CODE_NON_AUTHORITATIVE_INFORMATION
    NO_CONTENT = HTTP_CODE_NO_CONTENT
    RESET_CONTENT = HTTP_CODE_RESET_CONTENT
    PARTIAL_CONTENT = HTTP_CODE_PARTIAL_CONTENT
    MULTI_STATUS = HTTP_CODE_MULTI_STATUS
    ALREADY_REPORTED = HTTP_CODE_ALREADY_REPORTED
    IM_USED = HTTP_CODE_IM_USED
    MULTIPLE_CHOICES = HTTP_CODE_MULTIPLE_CHOICES
    MOVED_PERMANENTLY = HTTP_CODE_MOVED_PERMANENTLY
    FOUND = HTTP_CODE_FOUND
    SEE_OTHER = HTTP_CODE_SEE_OTHER
    NOT_MODIFIED = HTTP_CODE_NOT_MODIFIED
    USE_PROXY = HTTP_CODE_USE_PROXY
    TEMPORARY_REDIRECT = HTTP_CODE_TEMPORARY_REDIRECT
    PERMANENT_REDIRECT = HTTP_CODE_PERMANENT_REDIRECT
    BAD_REQUEST = HTTP_CODE_BAD_REQUEST
    UNAUTHORIZED = HTTP_CODE_UNAUTHORIZED
    FORBIDDEN = HTTP_CODE_FORBIDDEN
    NOT_FOUND = HTTP_CODE_NOT_FOUND
    CONFLICT = HTTP_CODE_CONFLICT
    UNPROCESSABLE_ENTITY = HTTP_CODE_UNPROCESSABLE_ENTITY
    INTERNAL_SERVER_ERROR = HTTP_CODE_INTERNAL_SERVER_ERROR


class HTTPStatusMessage(Enum):  # dead: disable
    """Enumerated HTTP response status message constants."""

    # 100 = 'Continue'
    # 101 = 'Switching Protocols'
    # 102 = 'Processing'
    # 103 = 'Early Hints'
    OK = "OK"
    CREATED = "Created"
    ACCEPTED = "Accepted"
    NON_AUTHORITATIVE_INFORMATION = "Non-Authoritative Information"
    NO_CONTENT = "No Content"
    RESET_CONTENT = "Reset Content"
    PARTIAL_CONTENT = "Partial Content"
    MULTI_STATUS = "Multi-Status"
    ALREADY_REPORTED = "Already Reported"
    IM_USED = "IM Used"
    MULTIPLE_CHOICES = "Multiple Choices"
    MOVED_PERMANENTLY = "Moved Permanently"
    FOUND = "Found"
    SEE_OTHER = "See Other"
    NOT_MODIFIED = "Not Modified"
    USE_PROXY = "Use Proxy"
    TEMPORARY_REDIRECT = "Temporary Redirect"
    PERMANENT_REDIRECT = "Permanent Redirect"
    BAD_REQUEST = "Bad Request"
    UNAUTHORIZED = "Unauthorized"
    # 402 = 'Payment Required'
    FORBIDDEN = "Forbidden"
    NOT_FOUND = "Not Found"
    # 405 = 'Method Not Allowed'
    # 406 = 'Not Acceptable'
    # 407 = 'Proxy Authentication Required'
    # 408 = 'Request Timeout'
    CONFLICT = "Conflict"
    # 410 = 'Gone'
    # 411 = 'Length Required'
    # 412 = 'Precondition Failed'
    # 413 = 'Content Too Large'
    # 414 = 'URI Too Long'
    # 415 = 'Unsupported Media Type'
    # 416 = 'Range Not Satisfiable'
    # 417 = 'Expectation Failed'
    # 418 = 'I\'m a teapot'
    # 421 = 'Misdirected Request'
    UNPROCESSABLE_ENTITY = "Unprocessable Entity"
    # 423 = 'Locked'
    # 424 = 'Failed Dependency'
    # 425 = 'Too Early'
    # 426 = 'Upgrade Required'
    # 428 = 'Precondition Required'
    # 429 = 'Too Many Requests'
    # 431 = 'Request Header Fields Too Large'
    # 451 = 'Unavailable For Legal Reasons'
    INTERNAL_SERVER_ERROR = "Internal Server Error"
    # 501 = 'Not Implemented'
    # 502 = 'Bad Gateway'
    # 503 = 'Service Unavailable'
    # 504 = 'Gateway Timeout'
    # 505 = 'HTTP Version Not Supported'
    # 506 = 'Variant Also Negotiates'
    # 507 = 'Insufficient Storage'
    # 508 = 'Loop Detected'
    # 510 = 'Not Extended'
    # 511 = 'Network Authentication Required'


"""Information response code group."""
HTTP_CODES_INFORMATIONAL: t.FrozenSet[t.List[int]] = frozenset([])

"""Successful response code group 2XX."""
HTTP_CODES_SUCCESSFUL = frozenset(
    [
        HTTPStatusCode.OK.value,
        HTTPStatusCode.CREATED.value,
        HTTPStatusCode.ACCEPTED.value,
        HTTPStatusCode.NON_AUTHORITATIVE_INFORMATION.value,
        HTTPStatusCode.NO_CONTENT.value,
        HTTPStatusCode.RESET_CONTENT.value,
        HTTPStatusCode.PARTIAL_CONTENT.value,
        HTTPStatusCode.MULTI_STATUS.value,
        HTTPStatusCode.ALREADY_REPORTED.value,
        HTTPStatusCode.IM_USED.value,
    ]
)

"""Redirection messages response code group 3XX."""
HTTP_CODES_REDIRECTIONS = frozenset(
    [
        HTTPStatusCode.MULTIPLE_CHOICES.value,
        HTTPStatusCode.MOVED_PERMANENTLY.value,
        HTTPStatusCode.FOUND.value,
        HTTPStatusCode.SEE_OTHER.value,
        HTTPStatusCode.NOT_MODIFIED.value,
        HTTPStatusCode.USE_PROXY.value,
        HTTPStatusCode.TEMPORARY_REDIRECT.value,
        HTTPStatusCode.PERMANENT_REDIRECT.value,
    ]
)

"""Client Error response code group 4XX."""
HTTP_CODES_CLIENT_ERRORS = frozenset(
    [
        HTTPStatusCode.BAD_REQUEST.value,
        HTTPStatusCode.UNAUTHORIZED.value,
        HTTPStatusCode.FORBIDDEN.value,
        HTTPStatusCode.NOT_FOUND.value,
        HTTPStatusCode.CONFLICT.value,
        HTTPStatusCode.UNPROCESSABLE_ENTITY.value,
    ]
)

"""Client Error response code group 5XX."""
HTTP_CODES_SERVER_ERRORS = frozenset([HTTPStatusCode.INTERNAL_SERVER_ERROR.value])

"""All available HTTP response codes."""
HTTP_CODES = frozenset(  # dead: disable
    [
        *HTTP_CODES_INFORMATIONAL,
        *HTTP_CODES_SUCCESSFUL,
        *HTTP_CODES_REDIRECTIONS,
        *HTTP_CODES_CLIENT_ERRORS,
        *HTTP_CODES_SERVER_ERRORS,
    ]
)


class BaseHTTPResponse(metaclass=abc.ABCMeta):  # dead: disable
    """Response content made by a named host, to a client."""

    pass
