from revproxy.views import ProxyView


class GraphanaProxyView(ProxyView):
    upstream = 'http://grafana:3000/dashboard/'

    def get_proxy_request_headers(self, request):
        headers = super(GraphanaProxyView, self).get_proxy_request_headers(
            request)
        headers['X-WEBAUTH-USER'] = request.user.email
        return headers
