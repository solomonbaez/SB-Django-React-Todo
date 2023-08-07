import {BrowserRouter, Route, Routes} from "react-router-dom";
import './App.css';
import Header from "./components/Header";
import Home from "./pages/Home";
import NotePage from "./pages/NotePage";

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Header/>
        <Routes>
          <Route path="/" element={<Home/>}/>
          <Route path="/note/:id" element={<NotePage/>}/>
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
