import React, {userState} from "react";

const BASE_URL = "http://localhost:8000/";

function NewPost(){
    const [image,setImage]=userState(null)
    const [title,setTitle]=userState('')
    const [creator,setCreator]=userState('')
    const [content,setContent]=userState('')

    return (
        <div className="newpost_content">
            <div className="newpost_image">
                <input className="newpost_image" type="filetype" id="filetype" placeholder="Choose Image" onClick={null}/>
            </div>
            <div className="newpost_title">
                <input className="newpost_title" type="text" id="title" placeholder="Title" onClick={(event)=>setTitle(event.target.value)} value={title}/>
            </div>
            <div className="newpost_creator">
                <input className="newpost_creator" type="text" id="creator" placeholder="Creator" onClick={(event)=>setCreator(event.target.value)} value={creator}/>
            </div>
            <div className="newpost_content">
                <textarea className="newpost_content" rows='10' id="content" placeholder="Description...." onClick={(event)=>setContent(event.target.value)}  value={content}/>
            </div>
            <div className="newpost_image">
                <button className="newpost_button" onClick={null}>Create Post</button>
            </div>
            
        </div>
    )
}

export default NewPost;