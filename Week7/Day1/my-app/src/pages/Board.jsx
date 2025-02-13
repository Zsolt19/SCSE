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
    const calculateWinner=(squares)=>{
        const lines=[
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]
        ];
        for (let i=0;i<lines.length;i++){
            const
        }
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