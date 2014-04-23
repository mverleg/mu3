

'''
    show a simple notification
    possibly inside another view, as confirmation or error
'''
def notification(request, message, subject = '', next = None):
    return render(request, 'notification.html', {
        'subject': subject,
        'message': message,
        'next': next,
    })


