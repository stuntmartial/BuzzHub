import React, { useState } from "react";
import "./CSS/Modals/educationpost.css";
import "./CSS/Modals/residencepost.css";
import "./CSS/Modals/personalinfo.css";
import "./CSS/Modals/workinfo.css";
import "./CSS/Modals/profileshowfriends.css";
import "./CSS/Modals/profilefriendrequests.css";
import Logo from "./Images/NewsFeed/icons/logo.svg";
import { TiTick } from "react-icons/ti";
import { MdCancel } from "react-icons/md";
import axios from "axios";


const BASE_URL = "http://127.0.0.1:8000/update/"

const EducationPost = () => {

  const defEduState = {
    eduField : '',
    eduConcentration : '',
    degree : '' 
  }

  const [ EduState , setEduState ] = useState(defEduState);

  const handleForm = (event) =>
  {
    event.preventDefault();

    if(event.target.name==="")
    {
      const data = {
        'educationField' : EduState.eduField, 
        'educationConcentration' : EduState.eduConcentration,
        'educationDegree' : EduState.degree
      }

      const headers = {
        'Authorization' : 'Bearer ' + localStorage.getItem('access_token')
      }

      axios(
        {
          method : 'post',
          url : BASE_URL + "education/",
          data : data,
          headers : headers
        }
      ).then(
        ((response)=>{
          window.location.reload()
        }),
        ((error)=>{console.log(error)})
      )
    }

    else
    {
      setEduState({
        ...EduState , 
        [event.target.name] : event.target.value 
      })
    }
  }

  return(
  <div className="education-container">
    <form className="education-form" onSubmit={handleForm}> 
    
      <div className="education-entry">
        <span className="education-span">Add Education Field</span>
        
        <input  className="education-input" 
                type="text"
                value={EduState.eduField}
                name="eduField"
                onChange={handleForm}
                >   
        </input>

      </div>
      
      <div className="education-entry">
        <span>Add Education Concentration</span>
        <input  className="education-input" 
                type="text"
                value={EduState.eduConcentration}
                name="eduConcentration"
                onChange={handleForm}
                >
        </input>
      </div>
      
      <div className="education-entry">
        <span>Degree</span>
        <input  className="education-input" 
                type="text"
                value={EduState.degree}
                name="degree"
                onChange={handleForm}
                >
        </input>
      </div>
      
      <div>
      <button className ="butt" type="submit">Submit</button>
      </div>
    </form>
    
  </div>
    )
}


const ResidencePost = () => {
  
  const defResState = {
    'hometown' : '',
    'locality' : ''
  }

  const [ ResState , setResState ] = useState(defResState);

  const handleForm = (event) =>
  {
    event.preventDefault()

    if(event.target.name==="")
    {

      const data = {
        'hometown' : ResState.hometown,
        'locality' : ResState.locality
      }

      const headers = {
        'Authorization' : 'Bearer ' + localStorage.getItem('access_token')
      }

      axios(
        {
          method : 'post',
          url : BASE_URL + 'residence/',
          data : data,
          headers : headers
        }
      ).then(
        ((response) =>
        {
          window.location.reload();
        }
        ),
        ((error)=>{console.log(error)})
      )
    }
    else
    {
      setResState(
        {
          ...ResState,
          [event.target.name] : event.target.value
        }
      )
    }
  }
  
  return(
  <div className="residence-container">
    <form className="residence-form" onSubmit={handleForm}> 
    
    <div className="residence-entry">
      <span className="residence-span">Hometown</span>
      <input  className="residence-input" 
              type="text"
              name="hometown"
              value={ResState.hometown}
              onChange={handleForm}
              >   
      </input>
      </div>
      <div className="residence-entry">
      <span>Locality</span>
      <input  className="residence-input"
              type="text"
              name="locality"
              value={ResState.locality}
              onChange={handleForm}
              >
      </input>
      </div>
      <div className="butt">
        <button type="submit">Submit</button>
      </div>

    </form>
    
  </div>
    )
}

const BdayModal = () => {

  const [bdayState , setbdayState] = useState(null)

  const handleForm = (event) =>
  {
    event.preventDefault()

    if(event.target.name==="")
    {
      
      const data = {
        'bday' : bdayState
      }

      const headers = {
        'Authorization' : 'Bearer ' + localStorage.getItem('access_token')
      }

      axios(
        {
          method : 'post',
          url : BASE_URL + 'bday/', 
          data : data,
          headers : headers,
        }
      ).then(
        ((response)=>{
          window.location.reload()
        }),
        ((error)=>{console.log(error)})
      )
    }
    else
    {
      setbdayState(event.target.value)
    }
  }

  return(
  <div className="personal-info-container">
    <form className="personal-info-form" onSubmit={handleForm}> 
    <div className="personal-info-entry">
      <span>Date-of-birth</span>
      <input  className="personal-info-input"
              type="text"
              value={bdayState}
              name="bday"
              onChange={handleForm}
              >
      </input>
      </div>
      <div>
        <button type="submit">Submit</button>
      </div>
    </form>
  </div>
    )
}

const GradYearModal = () => {

  const [gradYearState , setgradYearState] = useState(null)

  const handleForm = (event) =>
  {
    event.preventDefault()

    if(event.target.name==="")
    {
      const data = {
        'gradYear' : gradYearState
      }

      const headers = {
        'Authorization' : 'Bearer ' + localStorage.getItem('access_token')
      }

      axios(
        {
          method : 'post',
          url : BASE_URL + 'gradyear/', 
          data : data,
          headers : headers,
        }
      ).then(
        ((response)=>{
          window.location.reload()
        }),
        ((error)=>{console.log(error)})
      )
    }
    else
    {
      setgradYearState(event.target.value)
    }
  }

  return(
  <div className="personal-info-container">
    <form className="personal-info-form" onSubmit={handleForm}> 
    <div className="personal-info-entry">
      <span>Graduation Year</span>
      <input  className="personal-info-input"
              type="text"
              value={gradYearState}
              name="bday"
              onChange={handleForm}
              >
      </input>
      </div>
      <div>
        <button type="submit">Submit</button>
      </div>
    </form>
  </div>
    )
}

const BioModal = () => {
  
  const [bioState,setbioState] = useState(null)

  const handleForm = (event) =>
  {
    event.preventDefault()

    if(event.target.name==="")
    {
      const data = {
        'bio' : bioState
      }

      const headers = {
        'Authorization' : 'Bearer ' + localStorage.getItem('access_token')
      }

      axios(
        {
          method : 'post',
          url : BASE_URL + 'bio/', 
          data : data,
          headers : headers,
        }
      ).then(
        ((response)=>{
          window.location.reload()
        }),
        ((error)=>{console.log(error)})
      )
    }
    else
    {
      setbioState(event.target.value)
    }
  }

  return(
  <div className="personal-info-container">
    <form className="personal-info-form" onSubmit={handleForm}> 
    <div className="personal-info-entry">
      <span>Bio</span>
      <input  className="personal-info-input"
              type="text"
              value={bioState}
              name="bio"
              onChange={handleForm}
              >
      
      </input>
      </div>
      <div>
        <button type="submit">Submit</button>
      </div>
    </form>
  </div>
    )
}

const LangModal = () => {

  const [ langState , setlangState ] = useState('');

  const handleForm = (event) =>
  {
    event.preventDefault()

    if(event.target.name==="")
    {
      const data = {
        'lang' : langState
      }

      const headers = {
        'Authorization' : 'Bearer ' + localStorage.getItem('access_token')
      }

      axios(
        {
          method : 'post',
          url : BASE_URL + 'lang/', 
          data : data,
          headers : headers,
        }
      ).then(
        ((response)=>{
          window.location.reload()
        }),
        ((error)=>{console.log(error)})
      )
    }
    else
    {
      setlangState(event.target.value)
    }
  }

  return(
    <div className="personal-info-container">
      <form className="personal-info-form" onSubmit={handleForm}> 
      <div className="personal-info-entry">
        <span>Add Language</span>
        <input  className="personal-info-input"
                type="text"
                value={langState}
                name="lang"
                onChange={handleForm}
                >
        
        </input>
        </div>
        <div>
        <button type="submit">Submit</button>
      </div>
      </form>
    </div>
      )
}


const ProfilepicModal = () => {

  const [ picState , setpicState ] = useState('')

  const handleForm = (event) =>
  {
    event.preventDefault()

    console.log(event.target)

    if(event.target.name==="")
    {

      const formdata = new FormData()
      
      formdata.append('profile_pic',picState)

      const headers = {
        'Authorization' : 'Bearer ' + localStorage.getItem('access_token'),
        'Content-Type' : 'multipart/form-data'
      }

      console.log(formdata);

      axios(
        {
          method : 'post',
          url : BASE_URL + 'profile_pic/', 
          data : formdata,
          headers : headers,
        }
      ).then(
        ((response)=>{
          window.location.reload()
        }),
        ((error)=>{console.log(error)})
      )
    }
    else
    {
      
      setpicState(event.target.files[0])
      
    }
  }


  return(
    <div className="personal-info-container">
      <form className="personal-info-form" onSubmit={handleForm}> 
      <div className="personal-info-entry">
        <span>Profile Pic</span>
        <input  className="personal-info-input"
                type="file"
                name="profile_pic"
                onChange={handleForm}
                >
        </input>
        </div>
        <div>
        <button type="submit">Submit</button>
      </div>
      </form>
    </div>
      )
}

const SchoolModal = () => {
  
  const [ schoolState , setschoolState ] = useState('');

  const handleForm = (event) =>
  {
    event.preventDefault()

    if(event.target.name==="")
    {
      const data = {
        'school' : schoolState
      }

      const headers = {
        'Authorization' : 'Bearer ' + localStorage.getItem('access_token')
      }

      axios(
        {
          method : 'post',
          url : BASE_URL + 'school/', 
          data : data,
          headers : headers,
        }
      ).then(
        ((response)=>{
          window.location.reload()
        }),
        ((error)=>{console.log(error)})
      )
    }
    else
    {
      setschoolState(event.target.value)
    }
  }


  return(
    <div className="personal-info-container">
      <form className="personal-info-form" onSubmit={handleForm}> 
      <div className="personal-info-entry">
        <span>School</span>
        <input  className="personal-info-input"
                type="text"
                name="school"
                value={schoolState}
                onChange={handleForm}
                >
        
        </input>
        </div>
        <div>
        <button type="submit">Submit</button>
      </div>
      </form>
    </div>
      )
}


const WorkInfoPost = () => {
  
  const defWorkState = {
    'employer' : '',
    'workStartyear' : '',
    'workEndyear' : '',
    'workLocation' : '',
    'workPosition' : ''
  }
  
  const [ WorkState , setWorkState ] = useState(defWorkState);

  const handleForm = (event) =>
  {
    event.preventDefault();

    if(event.target.name==="")
    {
      const data = {
        'employer' : WorkState.employer,
        'workStartyear' : WorkState.workStartyear,
        'workEndyear' : WorkState.workEndyear,
        'workLocation' : WorkState.workLocation,
        'workPosition' : WorkState.workPosition
      }

      const headers = {
        'Authorization' : 'Bearer ' + localStorage.getItem('access_token')
      }

      axios(
        {
          method : 'post',
          url : BASE_URL + 'work/',
          data : data,
          headers : headers
        }
      ).then(
        ((response)=>{
          window.location.reload()
        }
        ),
        (
          (error)=>
          {
            console.log(error)
          }
        )
      )

    }
    else
    {
      setWorkState(
        {
          ...WorkState,
          [event.target.name] : event.target.value
        }
      )
    }


  }

  return(
  <div className="work-info-container">
    <form className="work-info-form" onSubmit={handleForm}> 
    <div className="work-info-entry">
      <span>Work Start Year</span>
      <input  className="work-info-input"
              type="number"
              min="2021"
              max="2043"
              step="1"
              name="workStartyear"
              value={WorkState.workStartyear}
              onChange={handleForm}
              >
      </input>
      </div>
    <div className="work-info-entry">
      <span className="work-info-span">Work End Year</span>
      <input  className="work-info-input"
              type="number"
              min="2010" 
              max="2026"
              step="1"
              name="workEndyear"
              value={WorkState.workEndyear}
              onChange={handleForm}
               >   
      </input>
      </div>
      <div className="work-info-entry">
      <span>Work Location</span>
      <input  className="work-info-input"
              type="text"
              name="workLocation"
              value={WorkState.workLocation}
              onChange={handleForm}
              >
      </input>
      </div>
      <div className="work-info-entry">
      <span>Work Position</span>
      <input  className="work-info-input"
              type="text"
              name="workPosition"
              value={WorkState.workPosition}
              onChange={handleForm}
              >
      </input>
      </div>
      <div className="work-info-entry">
      <span>Employer</span>
      <input  className="work-info-input"
              type="text"
              name="employer"
              value={WorkState.employer}
              onChange={handleForm}
              >
      </input>
      </div>
      <div className="butt">
        <button type="submit">Submit</button>
      </div>
    </form>
    
  </div>
    )
}

const LocaleModal = () =>
{

  const [ locale , setLocale] = useState('')

  const handleForm = (event) =>
  {
    event.preventDefault();
    console.log(event.target.name)
    
    if(event.target.name==="")
    {
      const data={
        'locale' : locale
      }

      const headers = {
        'Authorization' : 'Bearer ' + localStorage.getItem('access_token')
      }

      axios(
        {
          method : 'post',
          url : BASE_URL + "locale/",
          data : data,
          headers : headers

        }
      ).then(
        ((response)=>{
          window.location.reload()
        }),
        ((error)=>{console.log(error)})
      )

    }
    else
    {
      setLocale(event.target.value);
    }
  }

  return(
    <div className="work-info-container">
    <form className="work-info-form" onSubmit={handleForm}> 
    <div className="work-info-entry">
      <span>Add a place</span>
      <input  className="work-info-input"
              type="text"
              name="locale"
              value={locale}
              onChange={handleForm}
              >
      </input>
      <div className="butt">
        <button type="submit">Submit</button>
      </div>
      </div>
    </form>
    </div>
  )

}

export { 
  EducationPost ,
  WorkInfoPost,
  ResidencePost,
  LocaleModal,
  BioModal,
  ProfilepicModal,
  BdayModal,
  LangModal,
  SchoolModal,
  GradYearModal,
};

