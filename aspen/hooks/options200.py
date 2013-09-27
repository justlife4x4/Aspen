from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


from aspen import Response

def hook(request):
    """A hook to return 200 to an 'OPTIONS *' request"""
    if request.line.method == "OPTIONS" and request.line.uri == "*":
        raise Response(200)
    return request

