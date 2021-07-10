import React , { useState } from "react";
import { useHistory } from "react-router-dom";
import axios from "axios";
// import { makeStyles, Theme, createStyles } from '@material-ui/core/styles';
import Modal from '@material-ui/core/Modal';
import Backdrop from '@material-ui/core/Backdrop';
import Fade from '@material-ui/core/Fade';
import "./CSS/AddPost/AddPost.css";

//styles
// const useStyles = makeStyles((theme: Theme) =>
//   createStyles({
//     modal: {
//       display: 'flex',
//       alignItems: 'center',
//       justifyContent: 'center',
//     },
//     paper: {
//       backgroundColor: theme.palette.background.paper,
//       border: '2px solid #000',
//       boxShadow: theme.shadows[5],
//       padding: theme.spacing(2, 4, 3),
//     },
//   }),
// );

//component
const AddPost = ({ ShouldOpen, onClose }) =>
{

    const [ Caption , setCaption ] = useState();
    const [ ImageFile , setImageFile ] = useState();
    const [ open ,setOpen ] = useState(ShouldOpen);
    
    const history = useHistory();

    const handleOpen = () => {
        setOpen(true);
      };
    
      const handleClose = () => {
        setOpen(false);
        onClose(false);
      };

    const handleChange = (event) =>
    {
        console.log(event);
        console.log(event.target);
        event.preventDefault();
        if(event.target.name === "")
        {
            const formData = new FormData();
            formData.append('caption' , Caption);
            formData.append('image' , ImageFile);

            console.log(formData)

            const headers = {
                'Authorization' : 'Bearer ' + localStorage.getItem('access_token'),
                'Content-Type' : 'multipart/form-data'
            }

            axios(
                {
                    method : 'post',
                    url : 'http://127.0.0.1:8000/Post/createPost/',
                    data : formData,
                    headers : headers
                }
            ).then(
                (response) => {
                    console.log(response);
                    handleClose();
                    window.location.reload();
                    // history.push('/NewsFeed');
                },
                (error) => {console.log(error)}
            );
        }

        if(event.target.name === "Caption")
        {
            setCaption(event.target.value)
        }

        else if(event.target.name === "Image")
        {
            setImageFile(event.target.files[0])
        }
    }

    return(
        <>
            <button type="button" onClick={handleOpen}>
                Add Post
            </button>

            <Modal        
                    className="modal-st"
                    open={open}
                    onClose={handleClose}
                    closeAfterTransition
                    BackdropComponent={Backdrop}
                    BackdropProps={{
                    timeout: 500,
                    }}>
                <Fade in={open}>
                <div className="modal-form-holder">
                <form className="modal-form">                           
                    <div>
                    <textarea className="modal-input-space" type="text" name="Caption" value= {Caption} placeholder="What's on your mind !!" onChange={handleChange}/>
                    </div>
                    <div className="file-uploader">
                        <input type="file" name="Image" placeholder="Add Image" onChange={handleChange} />
                    </div>

                    <div>
                        <button className="modal-add-button" onClick={handleChange}> Add</button>
                    </div>

                </form>          
                
                </div>
                </Fade>
            </Modal>
        </>

    );
}

export default AddPost;
