import { React, useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
// import svg as react component
import { ReactComponent as Arrowleft } from "../assets/arrow-left.svg";

const getCookie = (cookie) => {
  const value = `; ${document.cookie}`;
  const sections = value.split(`; ${cookie}`);
  if (sections.length === 2) return sections.pop().split(";").shift();
};

const NotePage = () => {
  let noteId = useParams().id;
  let [note, setNote] = useState(null);
  let csrfToken = getCookie("csrftoken");

  const getNote = async () => {
    // prevent network issues on "create"
    if (noteId === "create") return;
    let response = await fetch(`/api/notes/${noteId}`);
    let data = await response.json();
    setNote(data);
  };

  const getTitle = (note) => {
    let title = note.description.split("\n")[0];
    if (title.length > 50) {
      title = title.splice(0, 50);
    }
    note.title = title;
  };

  const createNote = async () => {
    fetch(`/api/notes`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify(note),
    });
  };

  const updateNote = async () => {
    fetch(`/api/notes/${noteId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify(note),
    });
  };

  const deleteNote = async () => {
    fetch(`/api/notes/${noteId}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
    });
  };

  const handleSubmit = () => {
    // generate a title
    getTitle(note);

    if (noteId !== "create" && !note.description) {
      deleteNote();
    } else if (noteId !== "create") {
      updateNote();
    } else if (noteId === "create") {
      createNote();
    }
  };

  // inject noteId
  useEffect(() => {
    getNote();
  }, [noteId]);

  return (
    <div className="note">
      <div className="note-header">
        <h3>
          <Link to="/">
            <Arrowleft onClick={handleSubmit} />
          </Link>
        </h3>
        <h3>
          <Link to="/">
            {noteId !== "create" ? (
              <button onClick={deleteNote}>delete</button>
            ) : (
              <button onClick={handleSubmit}>create</button>
            )}
          </Link>
        </h3>
      </div>
      <textarea
        onChange={(e) => {
          setNote({
            ...note,
            description: e.target.value,
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
