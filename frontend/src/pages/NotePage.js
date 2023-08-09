import React from "react";
import { Routes, Route, useParams } from "react-router-dom";

const NotePage = () => {
  let params = useParams();
  return (
    <div>
      <h1>Test Note {params.id}</h1>
    </div>
  );
};

export default NotePage;
