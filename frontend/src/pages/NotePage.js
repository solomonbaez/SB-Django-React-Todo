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
    // prevent network issues on "create"
    if (noteId === "create") return;
    let response = await fetch(`/api/notes/${noteId}`);
    let data = await response.json();
    setNote(data);
  };

  const createNote = async () => {
    fetch(`/api/create/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(note),
    });
  };

  const updateNote = async () => {
    fetch(`/api/notes/${noteId}/update`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(note),
    });
  };

  const deleteNote = async () => {
    fetch(`/api/notes/${noteId}/delete`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    });
  };

  const handleSubmit = () => {
    if (noteId !== "create" && !note.description) {
      deleteNote();
    } else if (noteId !== "create") {
      updateNote();
    } else if (noteId === "create") {
      createNote();
    }
  };

  const handleDelete = () => {
    deleteNote();
  };

  return (
    <div className="note">
      <div className="note-header">
        <h3>
          <Link to="/">
            <Arrowleft onClick={handleSubmit} />
          </Link>
        </h3>
        {noteId !== "create" ? (
          <h3>
            <Link to="/">
              <button onClick={deleteNote}>delete</button>
            </Link>
          </h3>
        ) : (
          <h3>
            <Link to="/">
              <button onClick={handleSubmit}>create</button>
            </Link>
          </h3>
        )}
      </div>
      <textarea
        onChange={(e) => {
          setNote({
            ...note,
            description: e.target.value,
            title: e.target.value,
          });
        }}
        defaultValue={note?.description}
      >
        {note?.description}
      </textarea>
    </div>
  );
};

export default NotePage;
