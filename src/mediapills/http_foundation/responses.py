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

# 1XX Information response codes constants

"""This interim response indicates that the client should continue the request or ignore
the response if the request is already finished."""
HTTP_CODE_CONTINUE = 100

"""This code is sent in response to an Upgrade request header from the client and
indicates the protocol the server is switching to."""
HTTP_CODE_SWITCHING_PROTOCOLS = 101

"""This code indicates that the server has received and is processing the request, but
no response is available yet."""
HTTP_CODE_PROCESSING = 102

"""This status code is primarily intended to be used with the Link header, letting the
user agent start preloading resources while the server prepares a response."""
HTTP_CODE_EARLY_HINTS = 103

# 2XX Successful response codes constants

"""The request succeeded."""
HTTP_CODE_OK = 200

"""The request succeeded, and a new resource created as a result."""
HTTP_CODE_CREATED = 201

"""The request has been received but not yet acted upon. It is noncommittal, since there
is no way in HTTP to later send an asynchronous response indicating the outcome of the
request."""
HTTP_CODE_ACCEPTED = 202

"""This response code means the returned metadata is not exactly the same as is available
from the origin server, but is collected from a local or a third-party copy."""
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

# 3XX Redirection messages response codes constants

"""The request has more than one possible response."""
HTTP_CODE_MULTIPLE_CHOICES = 300

"""The URL of the requested resource has been changed permanently."""
HTTP_CODE_MOVED_PERMANENTLY = 301

"""This response code means that the URI of requested resource has been changed
temporarily."""
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

# 4XX Client error response codes constants

"""The server could not understand the request due to invalid syntax."""
HTTP_CODE_BAD_REQUEST = 400

"""Although the HTTP standard specifies 'unauthorized', semantically this response means
'unauthenticated'."""
HTTP_CODE_UNAUTHORIZED = 401

"""This response code is reserved for future use."""
HTTP_CODE_PAYMENT_REQUIRED = 402

"""The client does not have access rights to the content; that is, it is unauthorized, so
the server is refusing to give the requested resource."""
HTTP_CODE_FORBIDDEN = 403

"""The server can not find the requested resource. In the browser, this means
the URL is not recognized.
"""
HTTP_CODE_NOT_FOUND = 404

"""The request method is known by the server but is not supported by the target
resource."""
HTTP_CODE_METHOD_NOT_ALLOWED = 405

"""This response is sent when the web server, after performing server-driven content
negotiation, doesn't find any content that conforms to the criteria given by the user
agent."""
HTTP_CODE_NOT_ACCEPTABLE = 406

"""This is similar to 401 Unauthorized but authentication is needed to be done by a
proxy."""
HTTP_CODE_PROXY_AUTHENTICATION_REQUIRED = 407

"""This response is sent on an idle connection by some servers, even without any
previous request by the client. It means that the server would like to shut down this
unused connection."""
HTTP_CODE_REQUEST_TIMEOUT = 408

"""This response is sent when a request conflicts with the current state of the
server."""
HTTP_CODE_CONFLICT = 409

"""This response is sent when the requested content has been permanently deleted from
server, with no forwarding address."""
HTTP_CODE_GONE = 410

"""Server rejected the request because the Content-Length header field is not defined
and the server requires it."""
HTTP_CODE_LENGTH_REQUIRED = 411

"""The client has indicated preconditions in its headers which the server does not
meet."""
HTTP_CODE_PRECONDITION_FAILED = 412

"""Request entity is larger than limits defined by server."""
HTTP_CODE_REQUEST_ENTITY_TOO_LARGE = 413

"""The URI requested by the client is longer than the server is willing to interpret."""
HTTP_CODE_REQUEST_URI_TOO_LONG = 414

"""The media format of the requested data is not supported by the server, so the server
is rejecting the request."""
HTTP_CODE_UNSUPPORTED_MEDIA_TYPE = 415

"""The range specified by the Range header field in the request cannot be fulfilled."""
HTTP_CODE_REQUESTED_RANGE_NOT_SATISFIABLE = 416

"""This response code means the expectation indicated by the Expect request header field
cannot be met by the server."""
HTTP_CODE_EXPECTATION_FAILED = 417

"""The server refuses the attempt to brew coffee with a teapot."""
HTTP_CODE_I_AM_A_TEAPOT = 418

"""The request was directed at a server that is not able to produce a response."""
HTTP_CODE_MISDIRECTED_REQUEST = 421

"""The request was well-formed but was unable to be followed due to semantic errors."""
HTTP_CODE_UNPROCESSABLE_ENTITY = 422

"""The resource that is being accessed is locked."""
HTTP_CODE_LOCKED = 423

"""The request failed due to failure of a previous request."""
HTTP_CODE_FAILED_DEPENDENCY = 424

"""Indicates that the server is unwilling to risk processing a request that might be
replayed."""
HTTP_CODE_TOO_EARLY = 425

"""The server refuses to perform the request using the current protocol but might be
willing to do so after the client upgrades to a different protocol."""
HTTP_CODE_UPGRADE_REQUIRED = 426

"""The origin server requires the request to be conditional."""
HTTP_CODE_PRECONDITION_REQUIRED = 428

"""The user has sent too many requests in a given amount of time ("rate limiting")."""
HTTP_CODE_TOO_MANY_REQUESTS = 429

"""The server is unwilling to process the request because its header fields are too
large."""
HTTP_CODE_REQUEST_HEADER_FIELDS_TOO_LARGE = 431

"""The user agent requested a resource that cannot legally be provided, such as a web
page censored by a government."""
HTTP_CODE_UNAVAILABLE_FOR_LEGAL_REASONS = 451

# 5XX Server error response codes constants

"""The server has encountered a situation it does not know how to handle."""
HTTP_CODE_INTERNAL_SERVER_ERROR = 500

"""The request method is not supported by the server and cannot be handled."""
HTTP_CODE_NOT_IMPLEMENTED = 501

"""This error response means that the server, while working as a gateway to get a
response needed to handle the request, got an invalid response."""
HTTP_CODE_BAD_GATEWAY = 502

"""The server is not ready to handle the request."""
HTTP_CODE_SERVICE_UNAVAILABLE = 503

"""This error response is given when the server is acting as a gateway and cannot get a
response in time."""
HTTP_CODE_GATEWAY_TIMEOUT = 504

"""The HTTP version used in the request is not supported by the server."""
HTTP_CODE_VERSION_NOT_SUPPORTED = 505

"""The server has an internal configuration error: the chosen variant resource is
configured to engage in transparent content negotiation itself, and is therefore not a
proper end point in the negotiation process."""
HTTP_CODE_VARIANT_ALSO_NEGOTIATES_EXPERIMENTAL = 506

"""The method could not be performed on the resource because the server is unable to
store the representation needed to successfully complete the request."""
HTTP_CODE_INSUFFICIENT_STORAGE = 507

"""The server detected an infinite loop while processing the request."""
HTTP_CODE_LOOP_DETECTED = 508

"""Further extensions to the request are required for the server to fulfill it."""
HTTP_CODE_NOT_EXTENDED = 510

"""Indicates that the client needs to authenticate to gain network access."""
HTTP_CODE_NETWORK_AUTHENTICATION_REQUIRED = 511


class HTTPStatusCode(Enum):
    """Enumerated HTTP response codes constants."""

    # 1XX Status codes
    CONTINUE = HTTP_CODE_CONTINUE
    SWITCHING_PROTOCOLS = HTTP_CODE_SWITCHING_PROTOCOLS
    PROCESSING = HTTP_CODE_PROCESSING
    EARLY_HINTS = HTTP_CODE_EARLY_HINTS

    # 2XX Status codes
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

    # 3XX Status code
    MULTIPLE_CHOICES = HTTP_CODE_MULTIPLE_CHOICES
    MOVED_PERMANENTLY = HTTP_CODE_MOVED_PERMANENTLY
    FOUND = HTTP_CODE_FOUND
    SEE_OTHER = HTTP_CODE_SEE_OTHER
    NOT_MODIFIED = HTTP_CODE_NOT_MODIFIED
    USE_PROXY = HTTP_CODE_USE_PROXY
    TEMPORARY_REDIRECT = HTTP_CODE_TEMPORARY_REDIRECT
    PERMANENT_REDIRECT = HTTP_CODE_PERMANENT_REDIRECT

    # 4XX Status code
    BAD_REQUEST = HTTP_CODE_BAD_REQUEST
    UNAUTHORIZED = HTTP_CODE_UNAUTHORIZED
    PAYMENT_REQUIRED = HTTP_CODE_PAYMENT_REQUIRED
    FORBIDDEN = HTTP_CODE_FORBIDDEN
    NOT_FOUND = HTTP_CODE_NOT_FOUND
    METHOD_NOT_ALLOWED = HTTP_CODE_METHOD_NOT_ALLOWED
    NOT_ACCEPTABLE = HTTP_CODE_NOT_ACCEPTABLE
    PROXY_AUTHENTICATION_REQUIRED = HTTP_CODE_PROXY_AUTHENTICATION_REQUIRED
    REQUEST_TIMEOUT = HTTP_CODE_REQUEST_TIMEOUT
    CONFLICT = HTTP_CODE_CONFLICT
    GONE = HTTP_CODE_GONE
    LENGTH_REQUIRED = HTTP_CODE_LENGTH_REQUIRED
    PRECONDITION_FAILED = HTTP_CODE_PRECONDITION_FAILED
    REQUEST_ENTITY_TOO_LARGE = HTTP_CODE_REQUEST_ENTITY_TOO_LARGE
    REQUEST_URI_TOO_LONG = HTTP_CODE_REQUEST_URI_TOO_LONG
    UNSUPPORTED_MEDIA_TYPE = HTTP_CODE_UNSUPPORTED_MEDIA_TYPE
    REQUESTED_RANGE_NOT_SATISFIABLE = HTTP_CODE_REQUESTED_RANGE_NOT_SATISFIABLE
    EXPECTATION_FAILED = HTTP_CODE_EXPECTATION_FAILED
    I_AM_A_TEAPOT = HTTP_CODE_I_AM_A_TEAPOT
    MISDIRECTED_REQUEST = HTTP_CODE_MISDIRECTED_REQUEST
    UNPROCESSABLE_ENTITY = HTTP_CODE_UNPROCESSABLE_ENTITY
    LOCKED = HTTP_CODE_LOCKED
    FAILED_DEPENDENCY = HTTP_CODE_FAILED_DEPENDENCY
    TOO_EARLY = HTTP_CODE_TOO_EARLY
    UPGRADE_REQUIRED = HTTP_CODE_UPGRADE_REQUIRED
    PRECONDITION_REQUIRED = HTTP_CODE_PRECONDITION_REQUIRED
    TOO_MANY_REQUESTS = HTTP_CODE_TOO_MANY_REQUESTS
    REQUEST_HEADER_FIELDS_TOO_LARGE = HTTP_CODE_REQUEST_HEADER_FIELDS_TOO_LARGE
    UNAVAILABLE_FOR_LEGAL_REASONS = HTTP_CODE_UNAVAILABLE_FOR_LEGAL_REASONS

    # 5XX Status code
    INTERNAL_SERVER_ERROR = HTTP_CODE_INTERNAL_SERVER_ERROR
    NOT_IMPLEMENTED = HTTP_CODE_NOT_IMPLEMENTED
    BAD_GATEWAY = HTTP_CODE_BAD_GATEWAY
    SERVICE_UNAVAILABLE = HTTP_CODE_SERVICE_UNAVAILABLE
    GATEWAY_TIMEOUT = HTTP_CODE_GATEWAY_TIMEOUT
    VERSION_NOT_SUPPORTED = HTTP_CODE_VERSION_NOT_SUPPORTED
    VARIANT_ALSO_NEGOTIATES_EXPERIMENTAL = (
        HTTP_CODE_VARIANT_ALSO_NEGOTIATES_EXPERIMENTAL
    )
    INSUFFICIENT_STORAGE = HTTP_CODE_INSUFFICIENT_STORAGE
    LOOP_DETECTED = HTTP_CODE_LOOP_DETECTED
    NOT_EXTENDED = HTTP_CODE_NOT_EXTENDED
    NETWORK_AUTHENTICATION_REQUIRED = HTTP_CODE_NETWORK_AUTHENTICATION_REQUIRED


class HTTPStatusMessage(Enum):  # dead: disable
    """Enumerated HTTP response status message constants."""

    # 1XX Status codes
    CONTINUE = "Continue"
    SWITCHING_PROTOCOLS = "Switching Protocols"
    PROCESSING = "Processing"
    EARLY_HINTS = "Early Hints"

    # 2XX Status codes
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

    # 3XX Status code
    MULTIPLE_CHOICES = "Multiple Choices"
    MOVED_PERMANENTLY = "Moved Permanently"
    FOUND = "Found"
    SEE_OTHER = "See Other"
    NOT_MODIFIED = "Not Modified"
    USE_PROXY = "Use Proxy"
    TEMPORARY_REDIRECT = "Temporary Redirect"
    PERMANENT_REDIRECT = "Permanent Redirect"

    # 4XX Status code
    BAD_REQUEST = "Bad Request"
    UNAUTHORIZED = "Unauthorized"
    PAYMENT_REQUIRED = "Payment Required"
    FORBIDDEN = "Forbidden"
    NOT_FOUND = "Not Found"
    METHOD_NOT_ALLOWED = "Method Not Allowed"
    NOT_ACCEPTABLE = "Not Acceptable"
    PROXY_AUTHENTICATION_REQUIRED = "Proxy Authentication Required"
    REQUEST_TIMEOUT = "Request Timeout"
    CONFLICT = "Conflict"
    GONE = "Gone"
    LENGTH_REQUIRED = "Length Required"
    PRECONDITION_FAILED = "Precondition Failed"
    REQUEST_ENTITY_TOO_LARGE = "Content Too Large"
    REQUEST_URI_TOO_LONG = "URI Too Long"
    UNSUPPORTED_MEDIA_TYPE = "Unsupported Media Type"
    REQUESTED_RANGE_NOT_SATISFIABLE = "Range Not Satisfiable"
    EXPECTATION_FAILED = "Expectation Failed"
    I_AM_A_TEAPOT = "I'm a teapot"
    MISDIRECTED_REQUEST = "Misdirected Request"
    UNPROCESSABLE_ENTITY = "Unprocessable Entity"
    LOCKED = "Locked"
    FAILED_DEPENDENCY = "Failed Dependency"
    TOO_EARLY = "Too Early"
    UPGRADE_REQUIRED = "Upgrade Required"
    PRECONDITION_REQUIRED = "Precondition Required"
    TOO_MANY_REQUESTS = "Too Many Requests"
    REQUEST_HEADER_FIELDS_TOO_LARGE = "Request Header Fields Too Large"
    UNAVAILABLE_FOR_LEGAL_REASONS = "Unavailable For Legal Reasons"

    # 5XX Status code
    INTERNAL_SERVER_ERROR = "Internal Server Error"
    NOT_IMPLEMENTED = "Not Implemented"
    BAD_GATEWAY = "Bad Gateway"
    SERVICE_UNAVAILABLE = "Service Unavailable"
    GATEWAY_TIMEOUT = "Gateway Timeout"
    VERSION_NOT_SUPPORTED = "HTTP Version Not Supported"
    VARIANT_ALSO_NEGOTIATES_EXPERIMENTAL = "Variant Also Negotiates"
    INSUFFICIENT_STORAGE = "Insufficient Storage"
    LOOP_DETECTED = "Loop Detected"
    NOT_EXTENDED = "Not Extended"
    NETWORK_AUTHENTICATION_REQUIRED = "Network Authentication Required"


"""Information response code group."""
HTTP_CODES_INFORMATIONAL: t.FrozenSet[int] = frozenset(
    [
        HTTPStatusCode.CONTINUE.value,
        HTTPStatusCode.SWITCHING_PROTOCOLS.value,
        HTTPStatusCode.PROCESSING.value,
        HTTPStatusCode.EARLY_HINTS.value,
    ]
)

"""Successful response code group 2XX."""
HTTP_CODES_SUCCESSFUL: t.FrozenSet[int] = frozenset(
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
HTTP_CODES_REDIRECTIONS: t.FrozenSet[int] = frozenset(
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
HTTP_CODES_CLIENT_ERRORS: t.FrozenSet[int] = frozenset(
    [
        HTTPStatusCode.BAD_REQUEST.value,
        HTTPStatusCode.UNAUTHORIZED.value,
        HTTPStatusCode.PAYMENT_REQUIRED.value,
        HTTPStatusCode.FORBIDDEN.value,
        HTTPStatusCode.NOT_FOUND.value,
        HTTPStatusCode.METHOD_NOT_ALLOWED.value,
        HTTPStatusCode.NOT_ACCEPTABLE.value,
        HTTPStatusCode.PROXY_AUTHENTICATION_REQUIRED.value,
        HTTPStatusCode.REQUEST_TIMEOUT.value,
        HTTPStatusCode.CONFLICT.value,
        HTTPStatusCode.GONE.value,
        HTTPStatusCode.LENGTH_REQUIRED.value,
        HTTPStatusCode.PRECONDITION_FAILED.value,
        HTTPStatusCode.REQUEST_ENTITY_TOO_LARGE.value,
        HTTPStatusCode.REQUEST_URI_TOO_LONG.value,
        HTTPStatusCode.UNSUPPORTED_MEDIA_TYPE.value,
        HTTPStatusCode.REQUESTED_RANGE_NOT_SATISFIABLE.value,
        HTTPStatusCode.EXPECTATION_FAILED.value,
        HTTPStatusCode.I_AM_A_TEAPOT.value,
        HTTPStatusCode.MISDIRECTED_REQUEST.value,
        HTTPStatusCode.UNPROCESSABLE_ENTITY.value,
        HTTPStatusCode.LOCKED.value,
        HTTPStatusCode.FAILED_DEPENDENCY.value,
        HTTPStatusCode.TOO_EARLY.value,
        HTTPStatusCode.UPGRADE_REQUIRED.value,
        HTTPStatusCode.PRECONDITION_REQUIRED.value,
        HTTPStatusCode.TOO_MANY_REQUESTS.value,
        HTTPStatusCode.REQUEST_HEADER_FIELDS_TOO_LARGE.value,
        HTTPStatusCode.UNAVAILABLE_FOR_LEGAL_REASONS.value,
    ]
)

"""Client Error response code group 5XX."""
HTTP_CODES_SERVER_ERRORS: t.FrozenSet[int] = frozenset(
    [
        HTTPStatusCode.INTERNAL_SERVER_ERROR.value,
        HTTPStatusCode.INTERNAL_SERVER_ERROR.value,
        HTTPStatusCode.NOT_IMPLEMENTED.value,
        HTTPStatusCode.BAD_GATEWAY.value,
        HTTPStatusCode.SERVICE_UNAVAILABLE.value,
        HTTPStatusCode.GATEWAY_TIMEOUT.value,
        HTTPStatusCode.VERSION_NOT_SUPPORTED.value,
        HTTPStatusCode.VARIANT_ALSO_NEGOTIATES_EXPERIMENTAL.value,
        HTTPStatusCode.INSUFFICIENT_STORAGE.value,
        HTTPStatusCode.LOOP_DETECTED.value,
        HTTPStatusCode.NOT_EXTENDED.value,
        HTTPStatusCode.NETWORK_AUTHENTICATION_REQUIRED.value,
    ]
)

"""All available HTTP response codes."""
HTTP_STATUS_CODES: t.FrozenSet[int] = frozenset(
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
