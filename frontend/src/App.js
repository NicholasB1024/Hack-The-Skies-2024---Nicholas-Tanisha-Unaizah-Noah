import logo from './logo.svg';
import './App.css';
import React from 'react';
import { useState } from 'react';
import Header from './components/Header';
import LocationInput from './components/LocationInput';
import Directions from './components/Directions';
import Greeting from './components/Greeting';


function App() {
    const [directions, setDirections] = useState(null);
    const [searchData, setSearchData] = useState(null); // New state for user input

    const handleRouteSearch = async (data) => {
        try {
            setSearchData(data); // Save the user's input for display
            const response = await fetch('http://localhost:5000/api/find_route', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            });
            const result = await response.json();
            if (response.ok) {
                setDirections(result); // Save directions data
            } else {
                alert(result.error || 'An error occurred');
            }
        } catch (error) {
            console.error('Error fetching route:', error);
            alert('Failed to fetch route');
        }
    };

    return (
        <div>
            <Header />
            <main>
                <Greeting name="John" />
            </main>
            <LocationInput onSearch={handleRouteSearch} />
            {directions && <Directions directions={directions} />}
            {searchData && ( // Use searchData to display the input locations
                <div style={{ textAlign: 'center', marginTop: '20px' }}>
                    <h2>Searching for Routes</h2>
                    <p>
                        From: <strong>{searchData.pickup}</strong> <br />
                        To: <strong>{searchData.dropoff}</strong>
                    </p>
                </div>
            )}
        </div>
    );
}

export default App;



/*
export default App;

import React, { useState } from 'react';
import LocationInput from './components/LocationInput';
import Directions from './components/Directions';
import './App.css';

function App() {
    const [directions, setDirections] = useState(null);

    const handleRouteSearch = async (data) => {
        try {
            const response = await fetch('http://localhost:5000/api/find_route', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            });
            const result = await response.json();
            if (response.ok) {
                setDirections(result);
            } else {
                alert(result.error || 'An error occurred');
            }
        } catch (error) {
            console.error('Error fetching route:', error);
            alert('Failed to fetch route');
        }
    };

    return (
        <div className="App">
            <h1>PATHFINDR</h1>
            <LocationInput onSearch={handleRouteSearch} />
            {directions && <Directions directions={directions} />}
        </div>
    );
}

export default App; */

