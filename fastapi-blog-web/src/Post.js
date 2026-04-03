import React,{useState,useEffect} from "react";
import './Post.css'

const BASE_URL ="http://localhost:8000/"

function Post({postparam}){
    const [imageUrl,setImageUrl]=useState('')
    useEffect(()=>{
        setImageUrl(BASE_URL+postparam.image_url)
    },[])

    return (
        <div className="post">
            <img className="post_image" src={imageUrl}/>
        </div>
    )
}
export default Post