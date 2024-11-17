/*import React from 'react';

const Directions = ({ directions }) => {
    return (
        <div className="directions">
            <h2>Shortest Path Length: {directions.shortestPathLength}</h2>
            <h3>Directions:</h3>
            <ul className="list-group">
                {directions.directions.map((step, index) => (
                    <li className="list-group-item" key={index}>
                        {step}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Directions; */

import React from 'react';

const Directions = ({ directions }) => {
    return (
        <div className="directions">
            <h2>Shortest Path Length: {directions.shortestPathLength}</h2>
            <h3>Directions:</h3>
            <ul>
                {directions.directions.map((step, index) => (
                    <li key={index}>{step}</li>
                ))}
            </ul>
        </div>
    );
};

export default Directions;
