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
HTTP_RESPONSE_STATUS_CODE_OK = 200

"""The request succeeded, and a new resource created as a result."""
HTTP_RESPONSE_STATUS_CODE_CREATED = 201

"""The request has been received but not yet acted upon. It is noncommittal, since
there is no way in HTTP to later send an asynchronous response indicating the
outcome of the request."""
HTTP_RESPONSE_STATUS_CODE_ACCEPTED = 202

"""This response code means the returned metadata is not exactly the same as is
available from the origin server, but is collected from a local or a third-party
copy."""
HTTP_RESPONSE_STATUS_CODE_NON_AUTHORITATIVE_INFORMATION = 203

"""There is no content to send for this request, but the headers may be useful."""
HTTP_RESPONSE_STATUS_CODE_NO_CONTENT = 204

"""Tells the user agent to reset the document which sent this request."""
HTTP_RESPONSE_STATUS_CODE_RESET_CONTENT = 205

"""This response code is used when the Range header is sent from the client to request
only part of a resource."""
HTTP_RESPONSE_STATUS_CODE_PARTIAL_CONTENT = 206

"""Conveys information about multiple resources, for situations where multiple status
codes might be appropriate."""
HTTP_RESPONSE_STATUS_CODE_MULTI_STATUS = 207

"""Used inside a <dav:propstat> response element to avoid repeatedly enumerating the
internal members of multiple bindings to the same collection."""
HTTP_RESPONSE_STATUS_CODE_ALREADY_REPORTED = 208

"""The server has fulfilled a GET request for the resource, and the response is a
representation of the result of one or more instance-manipulations applied to the current
instance."""
HTTP_RESPONSE_STATUS_CODE_IM_USED = 226

# Redirection messages responses codes group

"""The request has more than one possible response."""
HTTP_RESPONSE_STATUS_CODE_MULTIPLE_CHOICES = 300

"""The URL of the requested resource has been changed permanently."""
HTTP_RESPONSE_STATUS_CODE_MOVED_PERMANENTLY = 301

"""This response code means that the URI of requested resource has been changed
temporarily.
"""
HTTP_RESPONSE_STATUS_CODE_FOUND = 302

"""The server sent this response to direct the client to get the requested resource at
another URI with a GET request."""
HTTP_RESPONSE_STATUS_CODE_SEE_OTHER = 303

"""This is used for caching purposes. It tells the client that the response has not been
modified, so the client can continue to use the same cached version of the response."""
HTTP_RESPONSE_STATUS_CODE_NOT_MODIFIED = 304

"""Defined in a previous version of the HTTP specification to indicate that a requested
response must be accessed by a proxy."""
HTTP_RESPONSE_STATUS_CODE_USE_PROXY = 305

"""This response code is no longer used; it is just reserved."""
HTTP_RESPONSE_STATUS_CODE_RESERVED = 306

"""The server sends this response to direct the client to get the requested resource at
another URI with same method that was used in the prior request."""
HTTP_RESPONSE_STATUS_CODE_TEMPORARY_REDIRECT = 307

"""This means that the resource is now permanently located at another URI, specified by
the Location: HTTP Response header."""
HTTP_RESPONSE_STATUS_CODE_PERMANENTLY_REDIRECT = 308

# Client error responses codes group

"""The server could not understand the request due to invalid syntax."""
HTTP_RESPONSE_STATUS_CODE_BAD_REQUEST = 400

"""Although the HTTP standard specifies 'unauthorized', semantically this
response means 'unauthenticated'.
"""
HTTP_RESPONSE_STATUS_CODE_UNAUTHORIZED = 401

"""The client does not have access rights to the content; that is, it is
unauthorized, so the server is refusing to give the requested resource.
"""
HTTP_RESPONSE_STATUS_CODE_FORBIDDEN = 403

"""The server can not find the requested resource. In the browser, this means
the URL is not recognized.
"""
HTTP_RESPONSE_STATUS_CODE_NOT_FOUND = 404

"""This response is sent when a request conflicts with the current state of the
server.
"""
HTTP_RESPONSE_STATUS_CODE_CONFLICT = 409

"""The request was well-formed but was unable to be followed due to semantic errors."""
HTTP_RESPONSE_STATUS_CODE_ENTITY = 422

# Server error responses codes group

"""The server has encountered a situation it does not know how to handle."""
HTTP_RESPONSE_STATUS_CODE_INTERNAL_SERVER_ERROR = 500


"""Information response code group."""
HTTP_RESPONSE_STATUS_CODES_INFORMATIONAL: t.FrozenSet[t.List[int]] = frozenset([])

"""Successful response code group."""
HTTP_RESPONSE_STATUS_CODES_SUCCESSFUL = frozenset(
    [
        HTTP_RESPONSE_STATUS_CODE_OK,
        HTTP_RESPONSE_STATUS_CODE_CREATED,
        HTTP_RESPONSE_STATUS_CODE_ACCEPTED,
        HTTP_RESPONSE_STATUS_CODE_NON_AUTHORITATIVE_INFORMATION,
        HTTP_RESPONSE_STATUS_CODE_NO_CONTENT,
        HTTP_RESPONSE_STATUS_CODE_RESET_CONTENT,
        HTTP_RESPONSE_STATUS_CODE_PARTIAL_CONTENT,
        HTTP_RESPONSE_STATUS_CODE_MULTI_STATUS,
        HTTP_RESPONSE_STATUS_CODE_ALREADY_REPORTED,
        HTTP_RESPONSE_STATUS_CODE_IM_USED,
    ]
)

"""Successful response code group."""
HTTP_RESPONSE_STATUS_CODE_REDIRECTIONS = frozenset(
    [
        HTTP_RESPONSE_STATUS_CODE_MULTIPLE_CHOICES,
        HTTP_RESPONSE_STATUS_CODE_MOVED_PERMANENTLY,
        HTTP_RESPONSE_STATUS_CODE_FOUND,
        HTTP_RESPONSE_STATUS_CODE_FOUND,
        HTTP_RESPONSE_STATUS_CODE_SEE_OTHER,
        HTTP_RESPONSE_STATUS_CODE_NOT_MODIFIED,
        HTTP_RESPONSE_STATUS_CODE_USE_PROXY,
        HTTP_RESPONSE_STATUS_CODE_RESERVED,
        HTTP_RESPONSE_STATUS_CODE_TEMPORARY_REDIRECT,
        HTTP_RESPONSE_STATUS_CODE_PERMANENTLY_REDIRECT,
    ]
)

"""Client Error response code group."""
HTTP_RESPONSE_STATUS_CODE_CLIENT_ERRORS = frozenset(
    [
        HTTP_RESPONSE_STATUS_CODE_BAD_REQUEST,
        HTTP_RESPONSE_STATUS_CODE_UNAUTHORIZED,
        HTTP_RESPONSE_STATUS_CODE_FORBIDDEN,
        HTTP_RESPONSE_STATUS_CODE_NOT_FOUND,
        HTTP_RESPONSE_STATUS_CODE_CONFLICT,
        HTTP_RESPONSE_STATUS_CODE_ENTITY,
    ]
)

"""Client Error response code group."""
HTTP_RESPONSE_STATUS_CODE_SERVER_ERRORS = frozenset(
    [HTTP_RESPONSE_STATUS_CODE_INTERNAL_SERVER_ERROR]
)

"""All available HTTP response codes."""
HTTP_RESPONSE_STATUS_CODES = frozenset(  # dead: disable
    [
        *HTTP_RESPONSE_STATUS_CODES_INFORMATIONAL,
        *HTTP_RESPONSE_STATUS_CODES_SUCCESSFUL,
        *HTTP_RESPONSE_STATUS_CODE_REDIRECTIONS,
        *HTTP_RESPONSE_STATUS_CODE_CLIENT_ERRORS,
        *HTTP_RESPONSE_STATUS_CODE_SERVER_ERRORS,
    ]
)


class HTTPResponseStatus(Enum):  # dead: disable
    """Enumerated HTTP response codes constants."""

    OK = HTTP_RESPONSE_STATUS_CODE_OK  # dead: disable
    CREATED = HTTP_RESPONSE_STATUS_CODE_CREATED  # dead: disable
    NO_CONTENT = HTTP_RESPONSE_STATUS_CODE_NO_CONTENT  # dead: disable
    FOUND = HTTP_RESPONSE_STATUS_CODE_FOUND  # dead: disable
    BAD_REQUEST = HTTP_RESPONSE_STATUS_CODE_BAD_REQUEST  # dead: disable
    UNAUTHORIZED = HTTP_RESPONSE_STATUS_CODE_UNAUTHORIZED  # dead: disable
    FORBIDDEN = HTTP_RESPONSE_STATUS_CODE_FORBIDDEN  # dead: disable
    NOT_FOUND = HTTP_RESPONSE_STATUS_CODE_NOT_FOUND  # dead: disable
    CONFLICT = HTTP_RESPONSE_STATUS_CODE_CONFLICT  # dead: disable
    ENTITY = HTTP_RESPONSE_STATUS_CODE_ENTITY  # dead: disable
    SERVER_ERROR = HTTP_RESPONSE_STATUS_CODE_INTERNAL_SERVER_ERROR  # dead: disable


class BaseHTTPResponse(metaclass=abc.ABCMeta):  # dead: disable
    """Response content made by a named host, to a client."""

    pass
