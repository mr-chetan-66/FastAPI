import "./App.css";
import React, { useEffect, useState } from "react";
import Post from "./Post";
import NewPost from "./NewPost";

const BASE_URL = "http://localhost:8000/";

function App() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch(BASE_URL + "post/get")
      .then((response) => {
        if (!response.ok) throw new Error("Network error");
        return response.json();
      })
      .then((data) => {
        setPosts(data.reverse());
      })
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="App">
      <div className="blog_title">City Blogs</div>

      <div className="app_post">
        {posts.map((singlePost) => (
          <Post
            key={singlePost.id}
            postparam={singlePost}
          />
        ))}
      </div>
      <div className="new_post">
        <NewPost/>
      </div>
    </div>
  );
}

export default App;