def karnameh():
    f = input('Enter your first name :')
    l = input('Enter your last name :')
    age = input('Enter your age :')
    ma = input('Enter your math score :')
    ph = input('Enter your physics score :')
    ch = input('Enter your chemistry score :')
    try:
        f = str(f)
        l = str(l)
        age = int(age)
        ma = float(ma)
        ph = float(ph)
        ch = float(ch)
    except:
        print('Enter the apporpriate data !!!')
        
        
    k = {'First name': f, 'Last name': l, 'Your age': age, 'Your math score': ma, 'Your physics score': ph, 'Your chemistry score': ch}
    return k