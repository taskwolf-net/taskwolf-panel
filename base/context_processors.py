from app.settings import ENVIRONMENT

def domain(request):
  if ENVIRONMENT == 'PRODUCTIVE':
    domain = 'taskwolf.net'
    request_prefix = 'https://team.taskwolf.net/v1'
  elif ENVIRONMENT == 'STAGING':
    domain = 'taskwolf.dev'
    request_prefix = 'https://team.taskwolf.dev/v1'
  elif ENVIRONMENT == 'LOCAL':
    domain = 'taskwolf.dev'
    request_prefix = 'http://10.96.0.9/v1'
  return {
    'domain': domain,
    'request_prefix': request_prefix
  }