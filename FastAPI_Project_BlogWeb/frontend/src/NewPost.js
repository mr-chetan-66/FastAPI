import React, { useState } from "react";
import "./NewPost.css";

const BASE_URL = "http://localhost:8000/";

function NewPost() {
  const [image, setImage] = useState(null);
  const [title, setTitle] = useState("");
  const [creator, setCreator] = useState("");
  const [content, setContent] = useState("");

  const setNewPostImage = (event) => {
    if (event.target.files && event.target.files[0]) {
      setImage(event.target.files[0]);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!image || !title || !creator || !content) {
      alert("All fields are required");
      return;
    }

    const formdata = new FormData();
    formdata.append("image", image);

    fetch(BASE_URL + "post/upload_file", {
      method: "POST",
      body: formdata,
    })
      .then((response) => {
        if (!response.ok) throw response;
        return response.json();
      })
      .then((data) => {
        createPost(data.filename);
      })
      .catch((error) => {
        console.log(error);
      })
      .finally(() => {
        setImage(null);
        document.querySelector(".newpost_image").value = "";
      });
  };

  const createPost = (filename) => {
    const json_str = JSON.stringify({
      image_url: filename,
      title: title,
      content: content,
      creator: creator,
    });

    fetch(BASE_URL + "post/add", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: json_str,
    })
      .then((response) => {
        if (!response.ok) throw response;
        return response;
      })
      .then(() => {
        setTitle("");
        setCreator("");
        setContent("");
        window.scrollTo(0, 0);
        window.location.reload(); // optional, works for now
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <div className="newpost_content">
      <input
        className="newpost_image"
        type="file"
        accept="image/*"
        onChange={setNewPostImage}
      />

      <input
        className="newpost_creator"
        type="text"
        placeholder="Creator"
        value={creator}
        onChange={(e) => setCreator(e.target.value)}
      />

      <input
        className="newpost_title"
        type="text"
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />

      <textarea
        className="newpost_content_text"
        rows="6"
        placeholder="Description..."
        value={content}
        onChange={(e) => setContent(e.target.value)}
      />

      <div className="newpost_button_div">
        <button className="newpost_button" onClick={handleSubmit}>
          Create Post
        </button>
      </div>
    </div>
  );
}

export default NewPost;