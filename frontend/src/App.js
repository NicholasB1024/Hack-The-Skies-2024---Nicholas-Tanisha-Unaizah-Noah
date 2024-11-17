import logo from './logo.svg';
import './App.css';
import React from 'react';
import { useState } from 'react';
import Header from './components/Header';
import LocationInput from './components/LocationInput';
import Greeting from './components/Greeting';

function App() {
  const [searchData, setSearchData] = useState(null);

    const handleSearch = (data) => {
        console.log('User input:', data); //logs the location and destination
        setSearchData(data);
    };

    return (
        <div>
            <Header />
            <main>
                <Greeting name = "John" />
            </main>
            <LocationInput onSearch={handleSearch} />
            {searchData && (
                <div style={{ textAlign: 'center', marginTop: '20px' }}>
                    <h2>Searching for Routes</h2>
                    <p>
                        From: <strong>{searchData.currentLocation}</strong> <br />
                        To: <strong>{searchData.destination}</strong>
                    </p>
                </div>
            )}
        </div>
    );
}



export default App;
