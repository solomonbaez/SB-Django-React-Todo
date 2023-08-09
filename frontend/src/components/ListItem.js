import React from "react";
import { Link } from "react-router-dom";

const ListItem = ({ note }) => {
  return (
    <Link to={`/note/${note.id}`}>
      <h3>{note.title}</h3>
    </Link>
  );
};

export default ListItem;
