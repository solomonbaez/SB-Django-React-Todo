import React, {useState, useEffect} from "react"

const Home = () => {

    // initialize state
    let [notes, setNotes] = useState([]);

    useEffect(() => {
        getNotes()
    }, [])

    let getNotes = async () => {
        // fetch requires async await
        let response = await fetch("http://127.0.0.1:8000/api/notes");
        let data = response.json();
        console.log("DATA:", data)
        setNotes(data)
    }
    
    return (
        <div className="App">
            Notes
        </div>
    )
}

export default Home