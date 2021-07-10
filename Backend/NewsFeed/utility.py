from Post_Management.utility import getPosts as getPostsfromProfile

def getPosts(connections , curr_profile):

    if len(connections) == 0 :
        return []

    posts = list()

    for profile in connections:
        postList = list(getPostsfromProfile(profile,curr_profile))
        
        for  post in postList:
            posts.append(dict(post))

    return posts
