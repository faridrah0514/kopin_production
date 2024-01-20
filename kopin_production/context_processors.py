from .lib.constant.constant import *

def default(request):
    return {
        'sidebar': SIDEBAR,
        'company_name': COMPANY_NAME
    }