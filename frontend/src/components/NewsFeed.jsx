import axios from "axios";
import { Link , useHistory } from "react-router-dom";
import { useState, useEffect  } from "react";
import Modal from "./Modal";
import {EducationPost, ResidencePost, WorkInfoPost , LocaleModal} from "./CustomModals";
import AddPost from "./AddPost";
import "./CSS/NewsFeed/PostFeedPage.css";
import { ReactComponent as PlusIcon } from "./Images/NewsFeed/icons/plus.svg";
import { ReactComponent as ChevronIcon } from "./Images/NewsFeed/icons/chevron.svg";
import { ReactComponent as BoltIcon } from "./Images/NewsFeed/icons/bolt.svg";
import {HiOutlineLogout} from "react-icons/hi";
import { FaThumbsUp } from "react-icons/fa";
import { MdComment } from "react-icons/md";
import { AiOutlineSend } from "react-icons/ai";
import { CgCloseR } from "react-icons/cg";

const BASE_URL = "http://127.0.0.1:8000/";


const Navbar = ({ username, profilepic }) => {

  const [ ProfileSearchState , setProfileSearchState ] = useState("");
  const [ profileSearchStatus , setprofileSearchStatus ] = useState("");
  const [modalOpen, SetModalOpen] = useState(false);

  let history = useHistory();
  const handleProfileSearch = (event) =>
  {
    event.preventDefault()

    if(event.target.name==="")
    {
      
      const headers = {
        'Authorization' : 'Bearer ' + localStorage.getItem('access_token')
      }

      const data = {
        'target_profile' : ProfileSearchState
      }

      let profileExistance=false;

      axios(
        {
          method : 'post',
          url : BASE_URL + "Profile/CheckProfile/"+ProfileSearchState+"/",
          data : data,
          headers : headers
        }
      ).then(
        (response)=>{
          profileExistance=response.data.profileExistance
          if(profileExistance===true)
            history.push("/Profile/"+ProfileSearchState)
          else
            setprofileSearchStatus("No profile found")
        },
        (errors)=>{console.log("Errors : ",errors)}
      )
    }
    else
    {
      setProfileSearchState(event.target.value);
    }
  }

  const handleLogout = () =>
  {
    axios(
      {
        method: 'post',
        url : BASE_URL + 'LogOut/',
        headers : {
          'Authorization' : 'Bearer ' + localStorage.getItem('access_token')
        }
      }
    ).then(
      ((response)=>{
        localStorage.removeItem('access_token')
        history.push("/Gateway")
      }
        ),
      ((error)=>console.log(error))
    )
  }

  return (
    <>
      {modalOpen ? (
        <AddPost onClose={SetModalOpen} ShouldOpen={modalOpen} />
      ) : (
        <div></div>
      )}
      <div className="Navbar-Container">
        <div className="Navbar">
          <div className="Nav-Right-Side">
            <img
              className="Logo"
              src="./poisa.svg"
              alt=""
              onClick={() => {
                alert("This is your NewsFeed. You can see posts from your friends in this window . You can even meet new people using this application !!!!");
              }}
            />

            <form onSubmit={handleProfileSearch}>
              <div className="SearchBarContainer">
                <input
                  name="Profile"
                  type="text"
                  placeholder="Search User"
                  value={ProfileSearchState}
                  onChange={handleProfileSearch}
                />
                <button type="submit" className="Submit-Button">
                  <span role="img" aria-label="">
                    🔍
                  </span>
                </button>
              </div>
            </form>
            <div className="search-return-text">{profileSearchStatus}</div>
          </div>
          <div className="Nav-Left-Side">
            
            <Link className="Goto-UserProfile" to={"/Profile/"+username}>
              <div className="logo-circle"> <img className="go_to_user_profilePic" src={"http://127.0.0.1:8000"+profilepic} alt="def"/> </div>
              <span className="Nav-Username">{username}</span>
            </Link>
            <button type="button" class="circle"  onClick={() => {
                SetModalOpen(!modalOpen);
              }}>
              <PlusIcon />
            </button>
            <button type="button" class="circle-2" onClick={handleLogout}>
              <HiOutlineLogout /> 
            </button>
            
          </div>
        </div>
      </div>
    </>
  );
};


const AddComment = ({postId}) => {

  const [ CommentState , setCommentState] = useState('')

  const handleSubmit = (event) =>
  {
    const data = {
      'comment' : CommentState,
      'post_id' : postId
    }

    const headers = {
      'Authorization' : 'Bearer ' + localStorage.getItem('access_token')
    }

    if(event.target.name==="")
    {
      axios(
        {
          method:'post',
          url:BASE_URL+"Post/commentPost/",
          data:data,
          headers:headers
        }
      ).then(
        ((response)=>{
          setCommentState('')
        }),
        ((error)=>{console.log(error)})
      )
    }
    else
    {
      setCommentState(event.target.value)
    }
  }
  
  return(
    <div className="render-comment">
      <form className="comment-form" onSubmit={handleSubmit}>

                <textarea
                  className="comment-input-space"
                  type="text"
                  name="CommentFORM"
                  value={CommentState}
                  placeholder="Write your comment..."
                  onChange={handleSubmit}
                />
                <button className="comment-butt">Comment</button>
                </form>
      </div>
  )
}

const Post = ({ ...props }) => {
  
  const [ postState , setpostState ] = useState({
    caption : props.caption,
    creator : props.creator,
    postCreatorImg : props.postCreatorImg,
    image : props.image,
    postId : props.postId,
    sharedBy : props.sharedBy,
    uploaded_time : props.uploaded_time,
    like_count : props.like_count,
    liked : props.alreadyLikedFlag,
    comment_count : props.comment_count,
    likeProfs : props.likeProfs,
    commentProfs : props.commentProfs,
    comments : props.comments,
              
  })
  
  const [showLikes , setshowLikes] = useState(false)
  const [showComments , setshowComments] = useState(false)

  const handleLike = (event) =>
  {
    let newState = postState
    newState.liked = !postState.liked
    setpostState(newState);
    
    if(postState.liked)
    {
      event.target.style.color = "blue";
      setpostState({...postState , ['like_count'] : postState.like_count+1 });
    }
    
    else
    {
    event.target.style.color = "white"
    setpostState({...postState , ['like_count'] : postState.like_count-1 });
    }

    const data = {
      liked_flag : postState.liked,
      post_id : postState.postId,
    }

    const headers = {
      'Authorization' : 'Bearer ' + localStorage.getItem('access_token')
    }

    axios(
      {
        method : "post",
        url : BASE_URL + "Post/likePost/",
        data : data,
        headers : headers
      }
    )

  }

  return (
    <div className="render-card">
      <Link to = {"/Profile/"+postState.creator}>
      <div className="profile-pic">
        
          <div className="profile-click">
          <img className="postCreatorImgProf" src={"http://127.0.0.1:8000" + postState.postCreatorImg} />
          </div>
          <span className="n-username-text">{postState.creator}</span>
        
        
      </div>
      </Link>
      <div className="card-content">{postState.caption}</div>
      {
        <div className="img_container">
          {props.image ? (
            <img className="container-img" src={postState.image} alt="" />
          ) : (
            <div></div>
          )}
        </div>
      }
      <hr className="new-hr" />
      <div className="actions-container">       
      <div className="button-space">
          <button type="button" name="butt1" 
                  className= {props.alreadyLikedFlag ?  "action_button_col_blue" : "action_button"}
                  onClick={handleLike}>
                    
                  <FaThumbsUp />
                  <div class="butt-text"> Like </div>
                  
          </button>
          <button type="button" class="numero_button" onClick={()=>{setshowLikes(!showLikes)}}>
            <span class="numero-text"> {postState.like_count} </span>
          </button>
      </div>      
      <div className="button-space">
          <button type="button" class="action_button" onClick={()=>{setshowComments(!showComments)}}>
            <MdComment />
            <span class="butt-text"> Comments </span>
          </button>
          
          <span class="numero-text"> {postState.comment_count} </span>
          
      </div>
      
      </div>
      <hr className="new-hr" />
    {showLikes ?
    <div className="LikeShow">
      {
        postState.likeProfs.map(
          (lP)=>
          {
            return(
              <>
                <p>{lP}</p>
              </>
            )
          }
        )
      }
    </div> : <div></div>}
    <AddComment postId={postState.postId}/>
    {showComments ? 
    <div className="CommentShow">
      {
        postState.comments.map(
          (comm,index)=>
          {
            return(
              <>
              <p>{postState.commentProfs[index]}</p>
              <p>{comm}</p>
              </>
            )
          }
        )
      }
    </div>:<div></div>}
    </div>
  );
};

const PostBody = ({ ...props }) => {

    const [modalEdu , setmodalEdu] = useState(false);
    const [modalRes , setmodalRes] = useState(false);
    const [modalWork , setmodalWork] = useState(false);
    const [modalLocale , setmodalLocale] = useState(false);

  return (
    <>
    <Modal ShouldOpen={modalEdu} Onclose={setmodalEdu}>
            <EducationPost />
    </Modal>

    <Modal ShouldOpen={modalRes} Onclose={setmodalRes}>
            <ResidencePost />
    </Modal>

    <Modal ShouldOpen={modalWork} Onclose={setmodalWork}>
            <WorkInfoPost />
    </Modal>

    <Modal ShouldOpen={modalLocale} Onclose={setmodalLocale}>
            <LocaleModal />
    </Modal>

    <div className="Post-Container">
      
          
      <div className="Post-Links">
        <div>
          <button type="button" class="ham_item"  onClick={ ()=>{setmodalEdu(true)} }>
            <span role="img" aria-label="" className="ham_button">
              📚
            </span>
            <span className="ham_txt">Education</span>
          </button>
          <button type="button" class="ham_item" onClick={ ()=>{setmodalRes(true)} }>
            <span role="img" aria-label="" className="ham_button">
              🏠
            </span>
            <span className="ham_txt">Residence</span>
          </button>
          <button type="button" class="ham_item" onClick={ ()=>{setmodalWork(true)} }>
            <span role="img" aria-label="" className="ham_button">
              💻
            </span>
            <span className="ham_txt">Work</span>
          </button>
          <button type="button" class="ham_item" onClick={ ()=>{setmodalLocale(true)} }>
            <span role="img" aria-label="" className="ham_button">
              🌏
            </span>
            <span className="ham_txt">Places you like to visit</span>
          </button>
        </div>
      </div>
      <div className="Actual-Posts-Container">
        {props.posts.map((post, index) => {
          return (
            <Post
              key={index}
              creator={post.creator}
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
              postCreatorImg={props.postProfPics[index].profile_pic}

            />
          );
        })}
      </div>

      <div className="Post-Suggestions">
        <div className="Post-Suggestions-inside">
          <font size="5" color="white">People you may know</font>
          {props.suggestions.map( (sugg,index)=>{
            return (
              <SuggBody
                key={index}
                suggestedProfile={sugg}

              />
            );
          }
          )}
        </div>
      </div>

    </div>
    </>
  );
};

const SuggBody = ({...props}) => {

  const [ sendReqFlag , setsendReqFlag ] = useState(false);
  const [ ignoredFlag , setignoredFlag ] = useState(false);
  const profileLink = '/Profile/' + props.suggestedProfile;
  
  const handlesendReq = () =>
  {
      const data = {
          'receiver' : props.suggestedProfile,
      };

      const headers = {
          'Authorization' : 'Bearer ' + localStorage.getItem('access_token')
      };

      axios(
          {
              method : 'post',
              url : BASE_URL + 'sendCon/',
              data : data,
              headers : headers
          }).then(
              (response) => {
                  setsendReqFlag(true);
              },
              (error) => (console.log(error))

          )
  }

  const handleIgnore = () =>
  {
    const data = {
      'ignoredProfile' : props.suggestedProfile
    }

    const headers = {
      'Authorization' : 'Bearer ' + localStorage.getItem('access_token')
    }
    
    axios(
      {
        method : 'post',
        url : BASE_URL + 'Ignore/',
        data : data,
        headers : headers
      }
    ).then(
      ((response)=>
      {
        setignoredFlag(true);    
      }),
      ((error)=>{console.log(error)})
    )
    
  }

  const SuggBodyuttons = () =>
  {
    return(
      <div className="suggestion-action">
      <button class="suggestion-button-accept" onClick={handlesendReq}>
        <AiOutlineSend />
        <span class="smol-text"> Add Friend </span>
      </button>
      <button class="suggestion-button-ignore" onClick={handleIgnore}>
        <CgCloseR />
        <span class="smol-text"> Ignore </span>
      </button>
    </div>
    )
  }

  return (
    <div className="Suggestion-holder">
      
      <div className="Suggestion-friend">
      
      <Link to={profileLink}>
        <span className="name-txt">{props.suggestedProfile}</span>
      </Link>
      </div>
      
    {
      (()=>{
        if(sendReqFlag===false && ignoredFlag===false) 
          return(<SuggBodyuttons />)
        else if(sendReqFlag===true)
          return(<span className="butt-text">Friend Request Sent</span>)
        else if(ignoredFlag===true)
          return(<span className="butt-text">Removed</span>)
      })()
    } 
    </div>
  );
};


const PostFeedPage = () => {

  const [ PostFeedState , setPostFeedState ] = useState({
    username : "",
    profilepic:null,
    posts : [],
    suggestions : [],
    postProfile_picNF : []
  }
  )
  
  const getProps = () => {
    const headers = {
      Authorization: "Bearer " + localStorage.getItem("access_token"),
    };

    axios({
      method: "get",
      url: BASE_URL + "getNewsFeedProps/",
      headers: headers,
    }).then(
      (response) => {
        setPostFeedState(
          {
            username : response.data.Profile,
            profilepic: response.data.Profile_pic.profile_pic,
            posts : response.data.Posts,
            suggestions : response.data.Suggestions,
            postProfile_picNF : response.data.postCreatorImgs
          }
        )
        
      },
      (error) => {
        console.log(error);
      }
    );
  };

  useEffect(getProps, []);

  return (
    <div className="feed-container">
      <Navbar username={PostFeedState.username} profilepic={PostFeedState.profilepic}/>
      <PostBody posts={PostFeedState.posts} suggestions={PostFeedState.suggestions} postProfPics={PostFeedState.postProfile_picNF} />
    </div>
  );
};

export default PostFeedPage;
export {Post};