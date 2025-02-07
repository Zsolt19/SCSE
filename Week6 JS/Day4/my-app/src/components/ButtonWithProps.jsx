import React from "react";

function ButtonWithProps(props) {
    const{buttonText}=props;
    //Destructure the 'buttonText' prop
    return (
        <button>{buttonText}</button>
    );
}

export default ButtonWithProps;