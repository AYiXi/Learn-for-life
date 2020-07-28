from mitmproxy import ctx

def request(flow):
    ctx.log.error(str(flow.request.url))

def response(flow):
    ctx.log.error(str(flow.response.status_code))
