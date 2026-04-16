import React from "react";
import "./Post.css";

const BASE_URL = "http://localhost:8000/";

function Post({ postparam, onDelete }) {
  const imageUrl = postparam.image_url
    ? BASE_URL + postparam.image_url
    : null;

  const handleDelete = () => {
    fetch(BASE_URL + `post/delete/${postparam.id}`, {
      method: "DELETE",
    })
      .then((response) => {
        if (!response.ok) throw response;
        return response;
      })
      .then(() => {
        onDelete(postparam.id); // ✅ notify parent
      })
      .catch((error) => {
        console.error("Delete failed:", error);
      });
  };

  return (
    <div className="post">
      {imageUrl && (
        <img
          className="post_image"
          src={imageUrl}
          alt={postparam.title || "Blog image"}
        />
      )}

      <div className="post_content">
        <h3 className="post_title">{postparam.title}</h3>
        <p className="post_creator">by {postparam.creator}</p>

        <p className="post_text">{postparam.content}</p>

        <div className="post_actions">
          <button
            className="delete_button"
            onClick={handleDelete}
          >
            Delete Post
          </button>
        </div>
      </div>
    </div>
  );
}

export default Post;
