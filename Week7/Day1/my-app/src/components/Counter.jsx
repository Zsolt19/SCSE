import React from "react";
import { useState } from "react";

const Counter = () => {
    const [count, setCount] = useState(0);
    return (
        <>
        <p>Counter: {count}</p>
        <button onClick={() => setCount(count + 1)}>Increment</button>
        <button onClick={() => setCount(count - 1)}>Decrement</button>
        </>
    );
}

export default Counter;
