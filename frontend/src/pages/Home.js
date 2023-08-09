import React, { useState, useEffect } from "react";
import ListItem from "../components/ListItem";

const Home = () => {
  // initialize state
  let [notes, setNotes] = useState([]);

  useEffect(() => {
    getNotes();
  }, []);

  let getNotes = async () => {
    // fetch requires async await
    let response = await fetch("/api/notes");
    let data = await response.json();
    console.log("DATA:", data);
    setNotes(data);
  };

  return (
    <div>
      <div className="notes-list">
        {notes.map((note, index) => (
          <ListItem key={index} note={note} />
        ))}
      </div>
    </div>
  );
};

export default Home;
