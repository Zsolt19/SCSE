import React, { useState } from "react";

const ColorClick = ({buttonText}) => {
  // State to manage the background color of the box
  const [boxColor, setBoxColor] = useState("lightblue");

  // Function to handle the button click
  const handleButtonClick = () => {
    // Prompt the user to enter a color
    const newColor = prompt("Enter a color (e.g., red, #00ff00, rgb(255, 0, 0)):");
    if (newColor) {
      // Update the box color if a valid input is provided
      setBoxColor(newColor);
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      {/* The box with dynamic background color */}
      <div
        style={{
          width: "200px",
          height: "200px",
          backgroundColor: boxColor,
          margin: "0 auto",
          border: "2px solid black",
        }}
      ></div>

      {/* Button to change the box color */}
      <button
        onClick={handleButtonClick}
        style={{ marginTop: "20px", padding: "10px 20px", fontSize: "16px" }}
      >
        {buttonText}
      </button>
    </div>
  );
};

export default ColorClick;