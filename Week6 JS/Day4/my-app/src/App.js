import logo from './logo.svg';
import './App.css';
import HomePage from "./components/HomePage.jsx";
import MyButton from './components/MyButton.jsx';
import ProfileCard from './components/ProfileCard.jsx';
import Counter from './components/Counter.jsx';
import ButtonWithProps from './components/ButtonWithProps.jsx';
import TestProfileCard from './components/TestProfileCard.jsx';
import ColourClick from './components/ColourClick.jsx';


function App() {
  return (
    <>
      <h1>Hello world!</h1>
      <HomePage />
      <MyButton />
      <img src="../components/Aaron.png" alt="profile" />
      <ProfileCard name="John Doe" age={29} role="Software Engineer"/>
      <ProfileCard imagg="./components/Aaron.png" name="Aaron Packer" age={29} role="Teacher"/>
      <ProfileCard name="Zsolt" age={29} role="Software Engineer"/>
      <TestProfileCard name="John Doe" age={29} bio="Software Engineer" role="Software Engineer"/>
      <ButtonWithProps buttonText="Click me"/>
      <ButtonWithProps buttonText="Don't click me"/>
      <ButtonWithProps buttonText="Click me too"/>
      <ButtonWithProps buttonText="Don't click me too"/>
      <ButtonWithProps buttonText="Click me three"/>
      <Counter />
      <ColourClick buttonText="Click to change colour" colour="red" />
    </>
  );
}

export default App;
