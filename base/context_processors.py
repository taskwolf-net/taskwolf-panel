from app.settings import ENVIRONMENT

def domain(request):
  if ENVIRONMENT == 'PRODUCTIVE':
    domain = 'dulno.com'
    request_prefix = 'https://team.dulno.com/v1'
  elif ENVIRONMENT == 'STAGING':
    domain = 'dulno.dev'
    request_prefix = 'https://team.dulno.dev/v1'
  elif ENVIRONMENT == 'LOCAL':
    domain = 'dulno.dev'
    request_prefix = 'http://10.96.0.9/v1'
  return {
    'domain': domain,
    'request_prefix': request_prefix
  }