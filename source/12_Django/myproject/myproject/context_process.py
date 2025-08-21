from datetime import datetime

def myproject(request):
    return {
        'now': datetime.now().strftime('%y-%m-%d %H:%M:%S'),
        

    }