import React from 'react';

function ProfileCard(props){
    const mystyle={
        color:"red",
        backgroundColor:"lightblue",
        padding: "10px",
        fontFamily: "Arial"
    };
    const{name}=props;
    const{age}=props;
    const{role}=props;
    const{imagg}=props;
    return(
        <>
            <h1 style={mystyle}>Profile Card</h1>
            <img src={imagg} alt="profile" />
            <p>Name: {name}</p>
            <p>Age: {age}</p>
            <p>Role: {role}</p>
        </>
    )
}

export default ProfileCard;
