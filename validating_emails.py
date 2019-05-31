def validator(email):
    #i did this try/exception to not allow emails without at and dot
    try:
        user, end = email.split('@')
        site, ext = end.split('.')
    except ValueError:
        return False
    
    #validation process start
    if not user.replace('_','').replace('-','').isalnum():
        return False
    elif not site.isalnum():
        return False
    elif len(ext) > 3:
        return False
    else:
        return True
    #validation finished

n = int(input())
emails = [input() for e in range(n)]

final_emails = list(filter(validator, emails))

print(sorted(final_emails))
