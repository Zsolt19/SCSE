import React from "react";

function TestProfileCard({name, age, bio, role}) {
    return (
        <div>
            <h1>{name}</h1>
            <p>{age}</p>
            <p>{bio}</p>
            <p>{role}</p>
        </div>
    );
}

export default TestProfileCard;