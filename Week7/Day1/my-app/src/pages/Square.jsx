import React from "react";
import {useState} from 'react';

// const Square=({props})=> {
//     return(
//         <>
//         <button className='square' onClick={props.onSquareClick}>
//             {props.value}
//         </button>
//         </>
//     )
// }

const Square=(props) =>{
    // const [squareText, setValue]=useState(null);
    // const handleClick=()=>{
    //     props.squareText('X')
    // }
    return(
        <button className='square' onClick={props.onSquareClick}>{props.squareText}</button>
    )
}

export default Square