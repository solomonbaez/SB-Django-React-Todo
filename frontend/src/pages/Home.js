import React, { useState, useEffect } from "react";
import ListItem from "../components/ListItem";
import AddButton from "../components/AddButton";

const Home = () => {
  // initialize state
  let [notes, setNotes] = useState([]);

  useEffect(() => {
    getNotes();
  }, []);

  const getNotes = async () => {
    // fetch requires async await
    let response = await fetch("/api/notes");
    let data = await response.json();
    console.log("DATA:", data);
    setNotes(data);
  };

  return (
    <div>
      <div className="notes">
        <div className="notes-header">
          <h2 className="notes-title">&#9782;notes</h2>
          <p className="notes-count">{notes.length}</p>
        </div>
        <div className="notes-list">
          {notes.map((note, index) => (
            <ListItem key={index} note={note} />
          ))}
        </div>
        <AddButton />
      </div>
    </div>
  );
};

export default Home;
