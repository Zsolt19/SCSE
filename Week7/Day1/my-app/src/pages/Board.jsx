import React from 'react'
import {useState} from 'react';
import Square from './Square';

const Board=()=>{
    const [xIsNext, setXIsNext]=useState(true);
    const [squares, setSquares]=useState(Array(9).fill(null));
    const handleClick=(i)=> {
        const nextSquares=squares.slice();
        if (squares[i]){
            return
        }
        if (xIsNext){
            nextSquares[i]='X';
        }else {
            nextSquares[i]='O';
        }
        // nextSquares[i]='X';
        setSquares(nextSquares);
        setXIsNext(!xIsNext);
    }
    return(
        <>
        <div class="status">Next player: X</div>
        <div className="board-row">
            <Square squareText={squares[0]} onSquareClick={()=>handleClick(0)}/>
            <Square squareText={squares[1]} onSquareClick={()=>handleClick(1)}/>
            <Square squareText={squares[2]} onSquareClick={()=>handleClick(2)}/>
        </div>
        <div className="board-row">
            <Square squareText={squares[3]} onSquareClick={()=>handleClick(3)}/>
            <Square squareText={squares[4]} onSquareClick={()=>handleClick(4)}/>
            <Square squareText={squares[5]} onSquareClick={()=>handleClick(5)}/>
        </div>
        <div className="board-row">
            <Square squareText={squares[6]} onSquareClick={()=>handleClick(6)}/>
            <Square squareText={squares[7]} onSquareClick={()=>handleClick(7)}/>
            <Square squareText={squares[8]} onSquareClick={()=>handleClick(8)}/>
        </div>
        </>
    )
}

export default Board