def convert(userdata):

    username = userdata['username']
    pname = userdata['profilename']
    flwrs = userdata['followers']  
    flwing = userdata['following']
    posts = userdata['posts']
    bio = userdata['bio']
    ppic = userdata['profilepic']
    extlink = userdata['extlink']
    accstat = userdata['privateaccount']
    

    #Finding username numbers ratio
    ratio_numusername = 0
    username = str(username)
    for char in username:
        if char.isdigit():
            ratio_numusername += 1

    u_ratio = ratio_numusername / len(username)

    #full name words count
    pname_count = len(pname.split())

    #ratio of number of numerical characters in profile name to its length
    ratio_numpname = 0
    pname = str(pname)
    if len(pname) > 0:
        for char in pname:
            if char.isdigit():
                ratio_numpname += 1

        ratio_numprofilename = ratio_numpname / len(pname)
    else:
        ratio_numprofilename = 0

    #if name==username
    if username == pname:
        nu = 1
    else:
        nu =0

    #bio length
    bio_len = len(bio)


    test_values = []
    test_values.insert(0, ppic)
    test_values.insert(1, u_ratio)
    test_values.insert(2, pname_count)
    test_values.insert(3, ratio_numprofilename)
    test_values.insert(4, nu)
    test_values.insert(5, bio_len)
    test_values.insert(6, extlink)
    test_values.insert(7, accstat)
    test_values.insert(8, int(posts))
    test_values.insert(9, int(flwrs))
    test_values.insert(10, int(flwing))

    return test_values