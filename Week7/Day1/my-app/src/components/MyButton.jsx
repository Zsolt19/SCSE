import React from "react";

function MyButton(props) {
    const {buttonText}=props

    return (
    <>
    <button>{buttonText}</button>
    </>
    );
}
export default MyButton;