import { React, useState, useEffect } from "react";
import { useParams } from "react-router-dom";

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
    <div>
      <p>{note?.description}</p>
    </div>
  );
};

export default NotePage;
