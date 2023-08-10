import React from "react";
import { Link } from "react-router-dom";

let getContent = (note) => {
  let content = note.description.replaceAll("\n", " ");
  content = content.replaceAll(note.title, "");

  if (content.length > 50) {
    return content.slice(0, 50) + "...";
  } else {
    return content;
  }
};

const ListItem = ({ note }) => {
  return (
    <Link to={`/note/${note.id}`}>
      <div className="notes-list-item">
        <h3>{note.title}</h3>
        <p>
          <span>{note.updated}</span>
          {getContent(note)}
        </p>
      </div>
    </Link>
  );
};

export default ListItem;
