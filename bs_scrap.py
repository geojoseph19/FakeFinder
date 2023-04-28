def scrap(prof_link):
    import json
    import requests
    from bs4 import BeautifulSoup

    # Username of the suspicious profile
    username = prof_link

    # URL to scrape
    url = f'https://www.instagram.com/{username}/'

    #Initializing Variables
    pname = ""
    flwrs = 0
    flwing = 0
    posts = 0
    bio = 0
    ppic = 0
    extlink = 0
    accstat = 0


    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the og:description meta tag
        mtag = soup.find('meta', {'name': 'description'})

    # print("Raw : ",mtag)
        
        mtag = str(mtag)
        mtag = mtag.replace('"',' ')
        mtag = mtag.split(" ")
        
        
    # pname = " ".join(mtag[15:-5])
        #Calculating followers count
        for i in range(len(mtag)):
            if mtag[i] == 'Followers,':
                flwrs = mtag[i-1]
                break
        flwrs = str(flwrs).replace(",","")
    
        #Calculating following count
        for i in range(len(mtag)):
            if mtag[i] == 'Following,':
                flwing = mtag[i-1]
                break
        flwing = str(flwing).replace(",","")
                
        #calculating posts count
        for i in range(len(mtag)):
            if mtag[i] == 'Posts':
                posts = mtag[i-1]
                break 
        posts = str(posts).replace(",","")

        
        #converting number abbrevations 
        flwrs = str(flwrs)
        if flwrs[-1] == "M":
            flwrs = flwrs[0:-1] 
            print(flwrs)
            flwrs = int(flwrs) * 1000000
        elif flwrs[-1] == "K":
            flwrs = flwrs[0:-1] 
            flwrs = int(flwrs) * 1000
            
            
    #---------------Capturing Bio--------------------------------

        # Find the <script> tag with type="application/ld+json"
        script_tag = soup.find("script", {"type": "application/ld+json"})

        #print(script_tag)

        # Extract the contents of the <script> tag 
        json_data = json.loads(script_tag.contents[0])

        #print(json_data)
        
        # Extract the "description" key from the JSON data
        bio = json_data["description"]

        #print(json.dumps(json_data, indent=2))

    #----------checking for profile picture-----------------------

        profile_img_url = json_data['author']['image']
    # print(profile_img_url)
        if profile_img_url == "":
            ppic = 0
        else:
            ppic = 1
            
    #-------------checking for external link-----------------------        
        
        ext_link_url = json_data['author']['sameAs']
    # print(ext_link_url)
        if ext_link_url == "":
            extlink = 0
        else:
            extlink = 1
            
            
            
    #-----------Checking account status(private/public)----------
        """
        #url to privatephotoviewer website
        url = f"https://privatephotoviewer.com/usr/{username}"

        # Send a GET request to the URL and get the HTML content
        response = requests.get(url)
        html_content = response.text

        # Parse the HTML content using BeautifulSoup
        soup2 = BeautifulSoup(html_content, "html.parser")

        # Find if any pics are publically  available
        pics = str(soup2.find('div', {'class': 'pic'}))
        print(pics)
        
        if int(posts) > 0 and pics =="None":
            print("Account is private")
        else:
            print("Account is public")

        #print(soup2) """
    

        #import requests

        headers = {"User-Agent": "Instagram 277.0.0.17.107 Android"}
        response = requests.get(f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}", headers=headers)
        if response.status_code in [200, 201]:
            # user account exists
            x = response.json()
            is_private = x["data"]["user"]["is_private"]
            if str(is_private) == "True":
                accstat = 1
            else:
                accstat = 0
            
        # print(json.dumps(x,indent=1))
        
        
    #--------If any data cannot be fetched through BeautifulSoup---------
        #Profile name
        pname = x["data"]["user"]["full_name"]
        #Following count
        if int(flwing) == 0:
            flwing = x["data"]["user"]["edge_follow"]['count']
            
        
        
        print("Username : ",username,"\nProfile name : ", pname, "\nFollowers : ", flwrs, 
            "\nFollowing : ", flwing, "\nPosts : ", posts,"\nBio : ", bio,"\nProfile pic : ",ppic,
            "\nExternal Link : ",extlink, "\nPrivate Account : ", accstat)
        
        user_data = {'username':username, 'profilename':pname, 'followers':flwrs,
                     'following':flwing, 'posts':posts, 'bio':bio, 'profilepic':ppic, 
                     'extlink':extlink, 'privateaccount':accstat}
        
    
    return user_data, profile_img_url






    #print(json.dumps(x,indent=1))
        
    #print(soup.prettify())
