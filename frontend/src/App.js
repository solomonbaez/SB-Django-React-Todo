import { HashRouter, Route, Routes } from "react-router-dom";
import "./App.css";
import Header from "./components/Header";
import Home from "./pages/Home";
import NotePage from "./pages/NotePage";

function App() {
  return (
    <HashRouter>
      <div className="container dark">
        <div className="app">
          <Header />
          <Routes>
            <Route path="/" exact element={<Home />} />
            <Route path="/note/:id" element={<NotePage />} />
          </Routes>
        </div>
      </div>
    </HashRouter>
  );
}

export default App;
