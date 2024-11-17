/*
import React, { useState } from 'react';

const LocationInput = ({ onSearch }) => {
    const [currentLocation, setCurrentLocation] = useState('');
    const [destination, setDestination] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        onSearch({ currentLocation, destination });
    };

    return (
        <form onSubmit={handleSubmit} style={{ textAlign: 'center', margin: '20px' }}>
            <div>
                <label>
                    Current Location:
                    <input
                        type="text"
                        value={currentLocation}
                        onChange={(e) => setCurrentLocation(e.target.value)}
                        placeholder="Enter your current location"
                        style={{ marginLeft: '10px', padding: '5px', width: '200px' }}
                    />
                </label>
            </div>
            <div style={{ marginTop: '10px' }}>
                <label>
                    Destination:
                    <input
                        type="text"
                        value={destination}
                        onChange={(e) => setDestination(e.target.value)}
                        placeholder="Enter your destination"
                        style={{ marginLeft: '10px', padding: '5px', width: '200px' }}
                    />
                </label>
            </div>
            <button type="submit" style={{ marginTop: '15px', padding: '20px 40px' }} className="floating-btn">
                Find Route
            </button>
        </form>
        
    );
};

export default LocationInput;
*/

import axios from "axios";
import React, { useState } from "react";

const LocationInput = ({ onSearch }) => {
    const [currentLocation, setCurrentLocation] = useState("");
    const [destination, setDestination] = useState("");
    const [result, setResult] = useState(null);
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            setError(null);
            const response = await axios.post("http://localhost:5000/api/find_route", {
                currentLocation,
                destination,
            });
            setResult(response.data);
            onSearch({ currentLocation, destination, result: response.data });
        } catch (err) {
            setError(err.response?.data?.error || "An error occurred");
            setResult(null);
        }
    };

    return (
        <div className="container mt-5">
            <form onSubmit={handleSubmit} className="p-4 bg-light rounded">
                <div className="form-group">
                    <label>Current Location</label>
                    <input
                        type="text"
                        className="form-control"
                        value={currentLocation}
                        onChange={(e) => setCurrentLocation(e.target.value)}
                        placeholder="Enter your current location"
                    />
                </div>
                <div className="form-group mt-3">
                    <label>Destination</label>
                    <input
                        type="text"
                        className="form-control"
                        value={destination}
                        onChange={(e) => setDestination(e.target.value)}
                        placeholder="Enter your destination"
                    />
                </div>
                <button type="submit" className="btn btn-primary mt-4">
                    Find Route
                </button>
            </form>
            {error && <div className="alert alert-danger mt-3">{error}</div>}
            {result && (
                <div className="mt-4">
                    <h4>Shortest Path Length: {result.shortestPathLength}</h4>
                    <h5>Directions:</h5>
                    <ul className="list-group">
                        {result.directions.map((dir, index) => (
                            <li className="list-group-item" key={index}>
                                {dir}
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
};

export default LocationInput;
