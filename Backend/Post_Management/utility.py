from .models import Content , Like , Comment
from django.db.models import Q
from .postSerializer import postSerializer

INIT_PATH = "http://127.0.0.1:8000"

def getPosts(profile , curr_profile):

    '''
        Get posts from a specific profile
        curr_profile : the profile to which the posts from
            "profile" is to be shown
    '''
    post_objects = Content.objects.filter(
        Q(creator = profile.user.username) 
    )

    
    post_objects_ids = list()
    alreadyLikedFlagList = list()

    for post in list(post_objects):
        
        post_objects_ids.append(post.postId)
        alreadyLikedFlag = Like.objects.filter(
            Q(postId=post.postId) & Q(liked_by=curr_profile)
            )

        if len(list(alreadyLikedFlag)) == 0:
            alreadyLikedFlag = False
        else:
            alreadyLikedFlag = True
        alreadyLikedFlagList.append(alreadyLikedFlag)

    post_objects = postSerializer(post_objects , many = True)

    count=0
    for postObj in post_objects.data:
        postObj['postId'] = post_objects_ids[count]
        postObj['image'] = INIT_PATH + postObj['image']
        postObj['alreadyLikedFlag'] = alreadyLikedFlagList[count]
        li = list(Like.objects.filter(postId=post_objects_ids[count]))
        li1 = [ i.liked_by.user.username for i in li ]
        postObj['likes'] = li1
        cm = list(Comment.objects.filter(postId=post_objects_ids[count]))
        cmprofs = [ i.commented_by.user.username for i in cm ]
        cmnts = [ i.comment for i in cm ]
        postObj['commentProfiles'] = cmprofs
        postObj['comments'] = cmnts
        count+=1

    return post_objects.data