def add_security_headers(response):
    # Content Security Policy (CSP)
    csp = (
        "script-src 'self'; "
    )
    response.headers['Content-Security-Policy'] = csp

    # Add other headers as needed
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'

    return response
