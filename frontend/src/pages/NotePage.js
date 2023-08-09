import { React, useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
// import svg as react component
import { ReactComponent as Arrowleft } from "../assets/arrow-left.svg";

const NotePage = () => {
  let noteId = useParams().id;
  let [note, setNote] = useState(null);

  // inject noteId
  useEffect(() => {
    getNote();
  }, [noteId]);

  const getNote = async () => {
    let response = await fetch(`/api/notes/${noteId}`);
    let data = await response.json();
    setNote(data);
  };

  return (
    <div className="note">
      <div className="note-header">
        <h3>
          <Link to="/">
            <Arrowleft />
          </Link>
        </h3>
      </div>
      <textarea defaultValue={note?.description}>{note?.description}</textarea>
    </div>
  );
};

export default NotePage;
