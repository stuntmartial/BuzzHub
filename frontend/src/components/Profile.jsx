import axios from "axios";
import React, { useState , useEffect } from "react";
import { Link , useParams } from "react-router-dom";
import { BioModal , BdayModal , SchoolModal , LangModal , ProfilepicModal , GradYearModal } from "./CustomModals"
import Modal from "./Modal";
import { Post } from "./NewsFeed";
import friendReq from "./Images/Profile/friendReq.png";
import friends from "./Images/Profile/friends.png";
import "./CSS/Profile/profile.css";
import { ImUserPlus } from "react-icons/im";
import { FaBirthdayCake , FaGraduationCap , FaSchool , FaUserFriends , FaAddressBook } from "react-icons/fa";
import { TiTick } from "react-icons/ti";
import { MdCancel } from "react-icons/md";
import { RiUserSharedFill } from "react-icons/ri";
import { GoDeviceCamera } from "react-icons/go";
import { GiPencil , GiConversation } from "react-icons/gi";

const BASE_URL = "http://127.0.0.1:8000/"

const EditProfile = () =>
{

  const [ BioModalState , setBioModalState ] = useState(false)
  const [ BdayModalState , setBdayModalState ] = useState(false)
  const [ SchoolModalState , setSchoolModalState ] = useState(false)
  const [ LangModalState , setLangModalState ] = useState(false)
  const [ gradYearModalState , setgradYearModalState ] = useState(false)
  const [ ProfilePicModalState , setProfilePicModalState ] = useState(false)

  return(
    <>
    <Modal ShouldOpen={BioModalState} Onclose={setBioModalState}>
      <BioModal />
    </Modal>

    <Modal ShouldOpen={BdayModalState} Onclose={setBdayModalState}>
      <BdayModal />
    </Modal>

    <Modal ShouldOpen={gradYearModalState} Onclose={setgradYearModalState}>
      <GradYearModal />
    </Modal>

    <Modal ShouldOpen={SchoolModalState} Onclose={setSchoolModalState}>
      <SchoolModal />
    </Modal>

    <Modal ShouldOpen={LangModalState} Onclose={setLangModalState}>
      <LangModal />
    </Modal>
    
    <Modal ShouldOpen={ProfilePicModalState} Onclose={setProfilePicModalState}>
      <ProfilepicModal />
    </Modal>


    <nav className="profile-navbar">
        <button className="profile-navbar-butt" onClick={()=>{setProfilePicModalState(true)}}>
          <GoDeviceCamera />
          <span className="profile-navbar-text"> Edit Profile Pic </span>
        </button>
        
        <button className="profile-navbar-butt" onClick={()=>{setBioModalState(true)}}>
          <GiPencil />
          <span className="profile-navbar-text"> Edit Bio </span>
        </button>
        
        <button className="profile-navbar-butt" onClick={()=>{setBdayModalState(true)}}>
          <FaBirthdayCake />
          <span className="profile-navbar-text"> Birthday </span>
        </button>

        <button className="profile-navbar-butt" onClick={()=>{setgradYearModalState(true)}}>
          <FaGraduationCap />
          <span className="profile-navbar-text"> Graduation Year </span>
        </button>
        
        <button className="profile-navbar-butt" onClick={()=>{setLangModalState(true)}}>
        <GiConversation/>
          <span className="profile-navbar-text"> Add Language </span>
        </button>

        <button className="profile-navbar-butt" onClick={()=>{setSchoolModalState(true)}}>
        <FaSchool/>
          <span className="profile-navbar-text"> School </span>
        </button>
        
    </nav>

  </>
  )
}

const ShowSingleFriend = ({...props}) =>
{
  const handleRemove = () =>
  {
    const data = {
      'other_end_user' : props.fname
    }

    const headers = {
      'Authorization' : 'Bearer ' + localStorage.getItem('access_token')
    }

    axios(
      {
        method : 'post',
        url : BASE_URL + 'delCon/',
        data : data,
        headers : headers
      }
    ).then
    (
      ((response)=>{
        window.location.reload()
      }
      ),
      ((error)=>{
        console.log(error)
        window.location.reload()
      }
      )
    )
  }

  return(
    
    <div className="pshow-friends-sub-container">
          <div className="pshow-friend-details">
            <div className="pshow-friend-profile-click">
              <img className="pshow-friend-profile-pic" src={friends} alt="def"/>
            </div>

            <div className="pshow-friend-name-txt">{props.fname}</div>
          </div>
        
        {
        props.MyProfile ?
          <div className="pshow-friend-action">
            <button class="pshow-friend-button-remove" onClick={handleRemove}>
              <MdCancel />
              <span class="pshow-friend-smol-text"> Remove Friend</span>
            </button>
          </div>
         : <div></div>
        }
    </div>
  )
}

const FriendRequests = ({...props}) =>
{
  const handleAccept = () =>
  {
    const data = {
      'sender' : props.fname
    }

    const headers = {
      'Authorization' : 'Bearer ' + localStorage.getItem('access_token')
    }

    axios(
      {
        method : 'post',
        url : BASE_URL + 'acceptCon/',
        data : data,
        headers : headers
      }
    ).then(
      ((response)=>
      {
        window.location.reload()
      }),
      ((error)=>
      {
        console.log(error)
        window.location.reload()
      })
    )

  }

  const handleReject = () =>
  {
    const data = {
      'sender' : props.fname
    }

    const headers = {
      'Authorization' : 'Bearer ' + localStorage.getItem('access_token')
    }

    axios(
      {
        method : 'post',
        url : BASE_URL + 'rejectCon/',
        data : data,
        headers : headers
      }
    ).then(
      ((response)=>
      {
        window.location.reload()
      }),
      ((error)=>
      {
        console.log(error)
        window.location.reload()
      })
    )

  }

  return(
    
    <div className="pshow-friends-sub-container">
          <div className="pshow-friend-details">
          <div className="pshow-friend-profile-click">

          <img className="pshow-friend-profile-pic" src={friendReq} alt=""/>
            </div>

            <div className="pshow-friend-name-txt">{props.fname}</div>
          </div>

        <div className="pshow-friend-action">
          <button class="pshow-friend-button-accept" onClick={handleAccept}>
            <TiTick />
            <span class="pshow-friend-smol-text"> Accept</span>
          </button>
          <button class="pshow-friend-button-remove" onClick={handleReject}>
            <MdCancel />
            <span class="pshow-friend-smol-text"> Reject</span>
          </button>
        </div>
      </div>
      
  )
}

const Profile = () =>
{
        const defaultProfileState = {
        'MyProfile' : false ,
        'Profilename' : '' ,
        'picObj' : null,
        'bio' : '',
        'Connections' : [] ,
        'Friend_Requests' : [] ,
        'AddFriendFlag' : false ,
        'EditFlag' : false ,
        'ConnectionReqFlag' : false,
        'posts' : []
    }

    const params = useParams()
    const req_Profile = params.req_Profile;
    const access_token = localStorage.getItem('access_token');

    const [ProfileState,setProfileState] = useState(defaultProfileState);
    const [FriendStatusButt , setFriendStatusButt] = useState("Show None");
    const [showConnectionState , setshowConnectionState] = useState(false);
    const [showConnectionReqState , setshowConnectionReqState] = useState(false);
    
    const handleAddFriend = () =>
    {
      const data = {
        'receiver' : req_Profile
      }

      const headers = {
        'Authorization' : 'Bearer ' + localStorage.getItem('access_token')
      }

      axios(
        {
          method : 'post',
          url : BASE_URL + "sendCon/",
          data : data,
          headers : headers
        }
      ).then(
        ((response)=>
          {
          window.location.reload();
          }),
        ((error) => 
          {
            console.log(error);
          }
        )
      )
    }

    const handleDelete = () =>
    {
      const data = {
        'other_end_user' : req_Profile
      }

      const headers = {
        'Authorization' : 'Bearer ' + localStorage.getItem('access_token')
      }

      axios(
        {
          method : 'post',
          url : BASE_URL + 'delCon/',
          data :data,
          headers : headers
        }
      ).then(
        ((response)=>
        {
          window.location.reload();
        }),
        ((error)=>{console.log(error)})
      )

    }

    const FriendStatRender = () =>
    {
      if(FriendStatusButt==="Show None")
        return(<div></div>)
      else if(FriendStatusButt==="Show Add Friend")
        return(
          <button className="profile-navbar-butt" onClick={handleAddFriend}>
            <ImUserPlus />
            <span className="profile-navbar-text"> Add Friend </span>
          </button>
        )
      else if(FriendStatusButt==="Connection Req Sent")
        return( 
          <button className="profile-navbar-butt" onClick={handleDelete}>
            <RiUserSharedFill />
            <span className="profile-navbar-text"> Request Sent </span>
          </button>
        )
      else if(FriendStatusButt==="Already Friends")
        return( 
          <button className="profile-navbar-butt" onClick={handleDelete}>
            <TiTick />
            <span className="profile-navbar-text"> Friends </span>
          </button>
        )
    }

    const getProps = () =>
    {
        axios(
            {
                method : 'get',
                url : 'http://127.0.0.1:8000/Profile/'+req_Profile+'/',
                headers : {'Authorization':'Bearer '+access_token}
            }
        ).then(
            (response) =>
            {   
                const updatedProfileState = {
                    'MyProfile' : response.data.MyProfile ,
                    'Profilename' : response.data.Username ,
                    'picObj' : response.data.picObj.profile_pic,
                    'bio' : response.data.bio,
                    'Connections' : response.data.Connections ,
                    'Friend_Requests' : response.data.Friend_Requests ,
                    'AddFriendFlag' : response.data.AddFriendFlag ,
                    'ConnectionReqFlag' : response.data.ConnectionReqFlag,
                    'EditFlag' : response.data.EditFlag ,
                    'posts' : response.data.posts,
                    'postCreatorImgs': response.data.postCreatorImgs
                };
                
                setProfileState(updatedProfileState);

                if(updatedProfileState.MyProfile===true)
                  setFriendStatusButt("Show None")
                else
                {
                  if(updatedProfileState.AddFriendFlag===true)
                    setFriendStatusButt("Show Add Friend")
                  else
                    {
                      if(updatedProfileState.ConnectionReqFlag===true)
                        setFriendStatusButt("Connection Req Sent")
                      else
                        setFriendStatusButt("Already Friends")
                    }
                    
                }
            },
            (error) => {console.log(error)}
        )

    }

  useEffect(getProps,[])

  return (
    <>
    <div className="sprofile">
      <div className="header-h1">Profile</div>
        <div className="profile-container">
          <div className="pshow-friends-holder">
          {showConnectionState ?
            
              <div className="pshow-friends-container">
              
                {             
                  ProfileState.Connections.map((conn,index)=>
                  {
                    return(
                      <ShowSingleFriend key={index}
                                        MyProfile={ProfileState.MyProfile}
                                        fname={conn} 
                                      
                      />
                    )
                  }
                  )
                }
          </div> : <div></div>              
          }
          </div>

    <div className="profile-sub-container">
      <div className="profile-about">
        <section id="container-about" className="container-about">
          <div className="sprofile-pic-container">
            <img className="sprofile-pic" src={"http://127.0.0.1:8000"+ProfileState.picObj} alt="abtimg" />
          </div>
          <div className="about-2">{ProfileState.Profilename}</div>
          <div className="about_txt_container" >
          <span className="about_txt">
            {ProfileState.bio}
          </span>
          </div>
        </section>
      </div>

      <nav className="profile-navbar">
         <FriendStatRender />
        <button className={showConnectionState?"profile-navbar-butt2":"profile-navbar-butt"} onClick={()=>setshowConnectionState(!showConnectionState)}>
          <FaUserFriends />
          <span className="profile-navbar-text">Friend List</span>
        </button>
        
        {ProfileState.EditFlag ?
        <>
        <button className={showConnectionReqState ? "profile-navbar-butt2" : "profile-navbar-butt"} onClick={()=>setshowConnectionReqState(!showConnectionReqState)}>
        <FaAddressBook />
          <span className="profile-navbar-text"> Friend Requests </span>
        </button></> : <div></div>} 
        
      </nav>
      
      {ProfileState.EditFlag ? <EditProfile /> : <div></div>}
      
      {
        ProfileState.posts.map((post,index)=>
        {
          return(
            <Post
              key={index}
              creator={post.creator}
              postCreatorImg={ProfileState.postCreatorImgs[index].profile_pic}
              caption={post.caption}
              image={post.image}
              uploaded_time={post.uploaded_time}
              sharedBy={post.sharedBy}
              postId={post.postId}
              alreadyLikedFlag={post.alreadyLikedFlag}
              like_count={post.like_count}
              comment_count={post.comment_count}
              likeProfs={post.likes}
              commentProfs={post.commentProfiles}
              comments={post.comments}
              

            />
          )
        })
      }
      
      </div>
      <div className="pshow-friends-holder">
      
      {
        (()=>{
          if(ProfileState.EditFlag)
          {
            if(showConnectionReqState)
              return(
                <div className="pshow-friends-container">
                {
                  ProfileState.Friend_Requests.map((conn,index)=>
                  {
                    return(
                        <FriendRequests key={index}
                                        fname={conn}                 
                        />
                    )
                  }
                )              
                }</div>
              )
            else
              return(<div></div>)
          }
          else
            return(<div></div>)

        })()
      }
      
      </div>
    </div> 
    </div>
    
  </>
  );
}


export default Profile;
